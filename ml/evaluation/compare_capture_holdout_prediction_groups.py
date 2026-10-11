
import json
from pathlib import Path

import numpy as np
import pandas as pd
from joblib import load

ROOT = Path(__file__).resolve().parents[2]

CAPTURE_PATH = (
    ROOT
    / "data/cicids2017/processed/"
    "cleaned_Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv"
)
MODEL_PATH = (
    ROOT
    / "ml/models/binary_random_forest_capture_holdout.joblib"
)
REPORT_PATH = (
    ROOT
    / "data/cicids2017/processed/"
    "binary_capture_holdout_report.json"
)
OUTPUT_PATH = (
    ROOT
    / "data/cicids2017/processed/"
    "capture_holdout_prediction_group_comparison.json"
)

CHUNK_SIZE = 50_000

FEATURES = [
    "Destination Port",
    "Flow Duration",
    "Total Fwd Packets",
    "Total Backward Packets",
    "Flow Bytes/s",
    "Flow Packets/s",
    "Packet Length Mean",
    "Init_Win_bytes_forward",
]

NUMERIC_COLUMNS = FEATURES

def main():
    model = load(MODEL_PATH)

    with REPORT_PATH.open("r", encoding="utf-8") as file:
        report = json.load(file)

    expected_features = report["feature_names"]

    if len(expected_features) != 77:
        raise ValueError(
            f"Expected 77 model features, found {len(expected_features)}."
        )

    if not hasattr(model, "predict"):
        raise TypeError("Loaded model does not provide predict().")

    # Keep reservoir samples bounded in memory.
    rng = np.random.default_rng(42)
    sample_limit = 100_000

    groups = {
        "missed_attacks": {
            "rows": 0,
            "labels": {},
            "samples": [],
        },
        "detected_attacks": {
            "rows": 0,
            "labels": {},
            "samples": [],
        },
        "benign_traffic": {
            "rows": 0,
            "labels": {},
            "samples": [],
        },
    }

    seen = {name: 0 for name in groups}
    offset = 0
    total_rows = 0

    for chunk in pd.read_csv(CAPTURE_PATH, chunksize=CHUNK_SIZE):
        chunk.columns = chunk.columns.str.strip()

        if "Label" not in chunk.columns:
            raise ValueError("Capture has no Label column.")

        missing = set(expected_features) - set(chunk.columns)
        if missing:
            raise ValueError(
                f"Capture is missing model features: {sorted(missing)}"
            )

        X = chunk[expected_features].copy()

        for column in expected_features:
            X[column] = pd.to_numeric(X[column], errors="coerce")

        X = X.replace([np.inf, -np.inf], np.nan)

        # Use NumPy to avoid feature-name warnings caused by this
        # saved model having been fitted on arrays.
        predictions = model.predict(X.to_numpy())

        labels = chunk["Label"].astype(str).str.strip()
        actual_attack = labels.ne("BENIGN").to_numpy()
        predicted_attack = np.asarray(predictions).astype(int) == 1

        masks = {
            "missed_attacks": actual_attack & ~predicted_attack,
            "detected_attacks": actual_attack & predicted_attack,
            "benign_traffic": ~actual_attack,
        }

        for group_name, mask in masks.items():
            group = groups[group_name]
            positions = np.flatnonzero(mask)

            group["rows"] += len(positions)

            for label, count in labels.iloc[positions].value_counts().items():
                group["labels"][label] = (
                    group["labels"].get(label, 0) + int(count)
                )

            # Reservoir sampling of records from each group.
            for position in positions:
                seen[group_name] += 1
                record = (
                    chunk.iloc[position][FEATURES]
                    .apply(pd.to_numeric, errors="coerce")
                    .to_dict()
                )

                if len(group["samples"]) < sample_limit:
                    group["samples"].append(record)
                else:
                    replacement = int(
                        rng.integers(0, seen[group_name])
                    )
                    if replacement < sample_limit:
                        group["samples"][replacement] = record

        total_rows += len(chunk)
        offset += len(chunk)
        print(f"Processed {total_rows:,} rows")

    results = {
        "capture": CAPTURE_PATH.name,
        "total_rows": total_rows,
        "sampling": {
            "method": "reservoir sampling",
            "seed": 42,
            "maximum_samples_per_group": sample_limit,
        },
        "groups": {},
    }

    for group_name, group in groups.items():
        sample = pd.DataFrame(group["samples"], columns=FEATURES)

        results["groups"][group_name] = {
            "rows": group["rows"],
            "original_label_counts": dict(
                sorted(group["labels"].items())
            ),
            "sample_rows": len(sample),
            "feature_summaries": {},
        }

        for feature in FEATURES:
            values = pd.to_numeric(
                sample[feature], errors="coerce"
            ).replace([np.inf, -np.inf], np.nan).dropna()

            results["groups"][group_name]["feature_summaries"][feature] = {
                "valid_sample_count": int(values.size),
                "missing_sample_count": int(sample[feature].isna().sum()),
                "median": (
                    float(values.median()) if len(values) else None
                ),
                "q25": (
                    float(values.quantile(0.25)) if len(values) else None
                ),
                "q75": (
                    float(values.quantile(0.75)) if len(values) else None
                ),
            }

    # Confirm all rows were assigned to exactly one group.
    grouped_rows = sum(group["rows"] for group in groups.values())
    if grouped_rows != total_rows:
        raise RuntimeError(
            f"Group total {grouped_rows} != capture total {total_rows}"
        )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8") as file:
        json.dump(results, file, indent=2, allow_nan=False)

    print("\nGroup totals:")
    for name, group in groups.items():
        print(f"  {name}: {group['rows']:,}")

    print(f"\nSaved comparison report: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
