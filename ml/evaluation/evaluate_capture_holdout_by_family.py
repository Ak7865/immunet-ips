
import json
from pathlib import Path

import joblib
import numpy as np
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data" / "cicids2017" / "processed"
MODEL_PATH = PROJECT_ROOT / "ml" / "models" / (
    "binary_random_forest_capture_holdout.joblib"
)
SOURCE_REPORT = DATA_DIR / "binary_capture_holdout_report.json"
OUTPUT_PATH = DATA_DIR / "binary_capture_holdout_by_family.json"

HELD_OUT_CAPTURE = (
    "cleaned_Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv"
)
CHUNK_SIZE = 50_000

ATTACK_FAMILIES = [
    "Web Attack Brute Force",
    "Web Attack XSS",
    "Web Attack Sql Injection",
]


def main():
    for path in [MODEL_PATH, SOURCE_REPORT, DATA_DIR / HELD_OUT_CAPTURE]:
        if not path.is_file():
            raise FileNotFoundError(f"Required file not found: {path}")

    with SOURCE_REPORT.open(encoding="utf-8") as file:
        source_report = json.load(file)

    if source_report.get("held_out_capture") != HELD_OUT_CAPTURE:
        raise ValueError("Source report refers to a different held-out capture.")

    model = joblib.load(MODEL_PATH)
    capture_path = DATA_DIR / HELD_OUT_CAPTURE

    family_counts = {
        family: {
            "actual": 0,
            "predicted_benign": 0,
            "predicted_attack": 0,
            "tp": 0,
            "fn": 0,
        }
        for family in ATTACK_FAMILIES
    }

    total_rows = 0
    total_attack = 0
    total_attack_predicted_benign = 0
    total_attack_predicted_attack = 0
    observed_labels = set()

    for chunk in pd.read_csv(
        capture_path,
        chunksize=CHUNK_SIZE,
        low_memory=False,
    ):
        chunk.columns = chunk.columns.str.strip()

        if "Label" not in chunk.columns:
            raise ValueError("Held-out capture has no Label column.")

        labels = chunk["Label"].astype("string").str.strip()

        if labels.isna().any():
            raise ValueError("Missing labels found in held-out capture.")

        observed_labels.update(labels.unique().tolist())

        original_features = [c for c in chunk.columns if c != "Label"]
        expected_features = source_report.get("feature_names")

        if not expected_features:
            raise ValueError(
                "Source report does not contain the expected feature names."
            )

        if len(expected_features) != model.n_features_in_:
            raise ValueError(
                f"Report contains {len(expected_features)} features, "
                f"but the model expects {model.n_features_in_}."
            )

        if original_features != expected_features:
            raise ValueError(
                "Held-out capture feature names or ordering do not match "
                "the source report."
            )

        X = chunk[expected_features].apply(pd.to_numeric, errors="coerce")
        X = X.replace([np.inf, -np.inf], np.nan)
        X = X.to_numpy(dtype=np.float64)


        predictions = model.predict(X)
        total_rows += len(chunk)

        attack_mask = labels.ne("BENIGN").to_numpy()
        predicted_attack = np.asarray(predictions) == 1
        predicted_benign = np.asarray(predictions) == 0

        total_attack += int(attack_mask.sum())
        total_attack_predicted_attack += int(
            (attack_mask & predicted_attack).sum()
        )
        total_attack_predicted_benign += int(
            (attack_mask & predicted_benign).sum()
        )

        for family in ATTACK_FAMILIES:
            family_mask = labels.eq(family).to_numpy()
            family_predicted_attack = family_mask & predicted_attack
            family_predicted_benign = family_mask & predicted_benign

            counts = family_counts[family]
            counts["actual"] += int(family_mask.sum())
            counts["predicted_attack"] += int(
                family_predicted_attack.sum()
            )
            counts["predicted_benign"] += int(
                family_predicted_benign.sum()
            )
            counts["tp"] += int(family_predicted_attack.sum())
            counts["fn"] += int(family_predicted_benign.sum())

    if total_rows != source_report["test_rows"]:
        raise ValueError(
            f"Expected {source_report['test_rows']} rows; got {total_rows}."
        )

    expected_attack = source_report["test_class_counts"]["ATTACK"]
    expected_fn = source_report["false_negatives"]
    expected_tp = source_report["confusion_matrix"][1][1]

    if total_attack != expected_attack:
        raise ValueError(
            f"Attack count mismatch: report={expected_attack}, "
            f"observed={total_attack}."
        )

    if total_attack_predicted_benign != expected_fn:
        raise ValueError(
            f"False-negative mismatch: report={expected_fn}, "
            f"observed={total_attack_predicted_benign}."
        )

    if total_attack_predicted_attack != expected_tp:
        raise ValueError(
            f"True-positive mismatch: report={expected_tp}, "
            f"observed={total_attack_predicted_attack}."
        )

    results = {}

    for family, counts in family_counts.items():
        actual = counts["actual"]
        recall = counts["tp"] / actual if actual else None

        results[family] = {
            **counts,
            "attack_recall": recall,
        }

    output = {
        "experiment": "Thursday WebAttacks capture holdout by original label",
        "held_out_capture": HELD_OUT_CAPTURE,
        "model_path": str(MODEL_PATH.relative_to(PROJECT_ROOT)),
        "total_rows": total_rows,
        "actual_attack_rows": total_attack,
        "attack_predicted_benign": total_attack_predicted_benign,
        "attack_predicted_attack": total_attack_predicted_attack,
        "attack_families": results,
        "observed_original_labels": sorted(observed_labels),
        "limitations": [
            "This is a diagnostic analysis, not an independent final test.",
            "Attack-family novelty and capture-level distribution shift remain confounded.",
            "Recall is undefined when a family has no actual records.",
        ],
    }

    OUTPUT_PATH.write_text(
        json.dumps(output, indent=2) + "\n",
        encoding="utf-8",
    )

    print("\n=== AGGREGATE ATTACK CHECK ===")
    print(f"Total rows: {total_rows:,}")
    print(f"Actual attacks: {total_attack:,}")
    print(f"Attacks predicted BENIGN: {total_attack_predicted_benign:,}")
    print(f"Attacks predicted ATTACK: {total_attack_predicted_attack:,}")

    print("\n=== ATTACK-FAMILY RESULTS ===")
    for family, counts in results.items():
        print(f"\n{family}")
        print(f"  Actual records: {counts['actual']:,}")
        print(f"  TP: {counts['tp']:,}")
        print(f"  FN: {counts['fn']:,}")
        print(f"  Predicted BENIGN: {counts['predicted_benign']:,}")
        print(f"  Predicted ATTACK: {counts['predicted_attack']:,}")

        if counts["attack_recall"] is not None:
            print(f"  Recall: {counts['attack_recall']:.4%}")
        else:
            print("  Recall: undefined (no actual records)")

    print(f"\nReport saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
