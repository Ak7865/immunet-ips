
import json
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix

PROJECT_ROOT = Path(__file__).resolve().parents[2]
PROCESSED_DIR = PROJECT_ROOT / "data" / "cicids2017" / "processed"
MODEL_PATH = PROJECT_ROOT / "ml" / "models" / "binary_random_forest.joblib"
REPORT_PATH = PROCESSED_DIR / "binary_capture_evaluation.json"

TEST_FILES = [
    "cleaned_Friday-WorkingHours-Morning.pcap_ISCX.csv",
    "cleaned_Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv",
    "cleaned_Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv",
]

CHUNK_SIZE = 100_000


def evaluate_capture(model, filename):
    path = PROCESSED_DIR / filename
    if not path.is_file():
        raise FileNotFoundError(f"Test file not found: {path}")

    y_true_parts = []
    y_pred_parts = []
    source_labels = {}

    for chunk in pd.read_csv(path, chunksize=CHUNK_SIZE, low_memory=False):
        labels = chunk["Label"].astype("string").str.strip()

        if labels.isna().any():
            raise ValueError(f"Missing labels found in {filename}")

        for label, count in labels.value_counts().items():
            source_labels[str(label)] = (
                source_labels.get(str(label), 0) + int(count)
            )

        features = chunk.drop(columns=["Label"]).to_numpy(
            dtype=np.float32,
            copy=True,
        )
        y_true = (labels != "BENIGN").to_numpy(dtype=np.int8)
        y_pred = model.predict(features).astype(np.int8)

        y_true_parts.append(y_true)
        y_pred_parts.append(y_pred)

    y_true = np.concatenate(y_true_parts)
    y_pred = np.concatenate(y_pred_parts)

    matrix = confusion_matrix(y_true, y_pred, labels=[0, 1])
    report = classification_report(
        y_true,
        y_pred,
        labels=[0, 1],
        target_names=["BENIGN", "ATTACK"],
        output_dict=True,
        zero_division=0,
    )

    return {
        "file": filename,
        "rows": int(len(y_true)),
        "source_label_counts": source_labels,
        "confusion_matrix": matrix.tolist(),
        "classification_report": report,
        "false_positives": int(matrix[0, 1]),
        "false_negatives": int(matrix[1, 0]),
    }


def main():
    if not MODEL_PATH.is_file():
        raise FileNotFoundError(
            f"Trained model not found: {MODEL_PATH}. "
            "Run the training script first."
        )

    model = joblib.load(MODEL_PATH)
    results = []

    for filename in TEST_FILES:
        print(f"\nEvaluating: {filename}")
        result = evaluate_capture(model, filename)
        results.append(result)

        report = result["classification_report"]
        print(f"Rows: {result['rows']:,}")
        print(f"False positives: {result['false_positives']:,}")
        print(f"False negatives: {result['false_negatives']:,}")

        for label in ("BENIGN", "ATTACK"):
            metrics = report[label]
            print(
                f"{label}: "
                f"precision={metrics['precision']:.4f}, "
                f"recall={metrics['recall']:.4f}, "
                f"F1={metrics['f1-score']:.4f}"
            )

    REPORT_PATH.write_text(
        json.dumps(results, indent=2),
        encoding="utf-8",
    )
    print(f"\nSaved per-capture results: {REPORT_PATH}")


if __name__ == "__main__":
    main()
