"""Inspect false-negative records from the capture-holdout experiment."""

import json
from pathlib import Path

import joblib
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "cicids2017" / "processed"

MODEL_PATH = (
    ROOT / "ml" / "models"
    / "binary_random_forest_capture_holdout.joblib"
)
REPORT_PATH = DATA_DIR / "binary_capture_holdout_report.json"
CAPTURE_PATH = (
    DATA_DIR
    / "cleaned_Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv"
)
OUTPUT_PATH = (
    DATA_DIR / "capture_holdout_false_negatives.csv"
)

CHUNK_SIZE = 50_000

SELECTED_FEATURES = [
    "Flow Duration",
    "Flow Bytes/s",
    "Flow Packets/s",
    "Init_Win_bytes_forward",
]

OUTPUT_COLUMNS = [
    "Capture_Row",
    "True_Label",
    "Predicted_Label",
    "Attack_Probability",
    *SELECTED_FEATURES,
    "Has_Negative_Duration",
    "Has_Negative_Byte_Rate",
    "Has_Negative_Packet_Rate",
    "Has_Missing_Rate",
]


def main():
    for path in [MODEL_PATH, REPORT_PATH, CAPTURE_PATH]:
        if not path.is_file():
            raise FileNotFoundError(f"Required file not found: {path}")

    with REPORT_PATH.open(encoding="utf-8") as file:
        report = json.load(file)

    if report.get("held_out_capture") != CAPTURE_PATH.name:
        raise ValueError("Report refers to a different held-out capture.")

    expected_features = report.get("feature_names")

    if not isinstance(expected_features, list) or not expected_features:
        raise ValueError("Report does not contain a valid feature list.")

    if len(expected_features) != 77:
        raise ValueError(
            f"Expected 77 report features; got {len(expected_features)}."
        )

    missing_selected = [
        name for name in SELECTED_FEATURES
        if name not in expected_features
    ]
    if missing_selected:
        raise ValueError(
            f"Selected features absent from report: {missing_selected}"
        )

    model = joblib.load(MODEL_PATH)

    if model.n_features_in_ != len(expected_features):
        raise ValueError(
            "Model input feature count does not match the report."
        )

    classifier = model.steps[-1][1]
    classes = list(classifier.classes_)

    if 1 not in classes:
        raise ValueError(f"Expected ATTACK class 1; found {classes}.")

    attack_column = classes.index(1)

    total_rows = 0
    false_negative_count = 0
    first_chunk = True

    # Start a fresh diagnostic output; do not modify the source data.
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_PATH.open("w", encoding="utf-8", newline="") as output_file:
        for chunk in pd.read_csv(
            CAPTURE_PATH,
            chunksize=CHUNK_SIZE,
            low_memory=False,
        ):
            chunk.columns = chunk.columns.str.strip()

            if "Label" not in chunk.columns:
                raise ValueError("Capture has no Label column.")

            original_features = [
                column for column in chunk.columns
                if column != "Label"
            ]

            if original_features != expected_features:
                raise ValueError(
                    "Capture feature names or ordering do not match "
                    "the report."
                )

            labels = chunk["Label"].astype("string").str.strip()

            if labels.isna().any():
                raise ValueError("Missing labels found in capture.")

            X = chunk[expected_features].apply(
                pd.to_numeric, errors="coerce"
            )
            X = X.replace([np.inf, -np.inf], np.nan)

            predictions = np.asarray(model.predict(X))
            probabilities = model.predict_proba(X)[:, attack_column]

            # A false negative is an actual attack predicted as BENIGN.
            false_negative_mask = (
                labels.ne("BENIGN").to_numpy()
                & (predictions == 0)
            )

            if false_negative_mask.any():
                selected = chunk.loc[
                    false_negative_mask, SELECTED_FEATURES
                ].copy()

                for feature in SELECTED_FEATURES:
                    selected[feature] = pd.to_numeric(
                        selected[feature], errors="coerce"
                    )

                selected = selected.replace(
                    [np.inf, -np.inf], np.nan
                )

                duration = selected["Flow Duration"]
                byte_rate = selected["Flow Bytes/s"]
                packet_rate = selected["Flow Packets/s"]

                row_numbers = np.arange(
                    total_rows + 1,
                    total_rows + len(chunk) + 1,
                )[false_negative_mask]

                result = pd.DataFrame({
                    "Capture_Row": row_numbers,
                    "True_Label": labels.to_numpy()[false_negative_mask],
                    "Predicted_Label": "BENIGN",
                    "Attack_Probability": probabilities[
                        false_negative_mask
                    ],
                    **{
                        feature: selected[feature].to_numpy()
                        for feature in SELECTED_FEATURES
                    },
                    "Has_Negative_Duration": (
                        duration.lt(0).fillna(False).to_numpy()
                    ),
                    "Has_Negative_Byte_Rate": (
                        byte_rate.lt(0).fillna(False).to_numpy()
                    ),
                    "Has_Negative_Packet_Rate": (
                        packet_rate.lt(0).fillna(False).to_numpy()
                    ),
                    "Has_Missing_Rate": (
                        byte_rate.isna() | packet_rate.isna()
                    ).to_numpy(),
                }, columns=OUTPUT_COLUMNS)

                result.to_csv(
                    output_file,
                    index=False,
                    header=first_chunk,
                )
                first_chunk = False
                false_negative_count += len(result)

            total_rows += len(chunk)

            print(
                f"Scanned {total_rows:,} rows; "
                f"false negatives found: {false_negative_count:,}",
                flush=True,
            )

    expected_rows = report.get("test_rows")
    expected_fn = report.get("false_negatives")

    if total_rows != expected_rows:
        raise ValueError(
            f"Capture row mismatch: report={expected_rows}, "
            f"scanned={total_rows}."
        )

    if false_negative_count != expected_fn:
        raise ValueError(
            f"False-negative mismatch: report={expected_fn}, "
            f"observed={false_negative_count}. "
            f"Inspect {OUTPUT_PATH} before relying on the output."
        )

    print("\nDiagnostic completed successfully.")
    print(f"Capture rows scanned: {total_rows:,}")
    print(f"False-negative records: {false_negative_count:,}")
    print(f"Output: {OUTPUT_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
