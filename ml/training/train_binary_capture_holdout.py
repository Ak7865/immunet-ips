
import json
import time
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.pipeline import Pipeline


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data" / "cicids2017" / "processed"
MODEL_DIR = PROJECT_ROOT / "ml" / "models"

HELD_OUT_CAPTURE = (
    "cleaned_Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv"
)

TRAINING_CAPTURES = [
    "cleaned_Monday-WorkingHours.pcap_ISCX.csv",
    "cleaned_Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv",
    "cleaned_Tuesday-WorkingHours.pcap_ISCX.csv",
    "cleaned_Wednesday-workingHours.pcap_ISCX.csv",
]

CHUNK_SIZE = 100_000
TRAINING_SAMPLE_SIZE = 300_000
RANDOM_STATE = 42

MODEL_PATH = MODEL_DIR / "binary_random_forest_capture_holdout.joblib"
REPORT_PATH = DATA_DIR / "binary_capture_holdout_report.json"


def iter_csv_chunks(path: Path):
    """Read a processed capture in chunks and return numeric features."""
    for frame in pd.read_csv(path, chunksize=CHUNK_SIZE, low_memory=False):
        frame.columns = frame.columns.str.strip()

        if "Label" not in frame.columns:
            raise ValueError(f"Missing Label column in {path.name}")

        labels = frame.pop("Label").astype("string").str.strip()

        if labels.isna().any():
            raise ValueError(f"Missing labels in {path.name}")

        y = (labels != "BENIGN").astype(np.int8).to_numpy()

        frame = frame.apply(pd.to_numeric, errors="coerce")
        frame = frame.replace([np.inf, -np.inf], np.nan)

        yield frame, y


def main():
    started = time.time()
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    held_out_path = DATA_DIR / HELD_OUT_CAPTURE
    training_paths = [DATA_DIR / name for name in TRAINING_CAPTURES]

    if not held_out_path.is_file():
        raise FileNotFoundError(f"Held-out capture not found: {held_out_path}")

    for path in training_paths:
        if not path.is_file():
            raise FileNotFoundError(f"Training capture not found: {path}")

    if held_out_path in training_paths:
        raise ValueError("Held-out capture must not be used for training.")

    # Verify the feature schema before sampling or fitting.
    expected_features = None

    for path in [*training_paths, held_out_path]:
        header = pd.read_csv(path, nrows=0)
        columns = header.columns.str.strip().tolist()

        if columns.count("Label") != 1:
            raise ValueError(f"Expected exactly one Label column in {path.name}")

        features = [column for column in columns if column != "Label"]

        if expected_features is None:
            expected_features = features
        elif features != expected_features:
            raise ValueError(
                f"Feature schema mismatch in {path.name}. "
                "Column names and order must match."
            )

    if len(expected_features) != 77:
        raise ValueError(
            f"Expected 77 features but found {len(expected_features)}."
        )

    print(f"Verified feature count: {len(expected_features)}")

    # Reproducible key-based sampling. Keep the 300,000 lowest random keys
    # across all eligible training captures.
    rng = np.random.default_rng(RANDOM_STATE)
    sample_keys = np.empty(0, dtype=np.float64)
    sample_X = np.empty(
        (0, len(expected_features)), 
        dtype=np.float32
    )
    sample_y = np.empty(0, dtype=np.int8)

    source_class_counts = {0: 0, 1: 0}
    source_rows = 0

    for path in training_paths:
        print(f"Scanning training capture: {path.name}")

        for frame, y_chunk in iter_csv_chunks(path):
            if frame.columns.tolist() != expected_features:
                raise ValueError(f"Feature schema changed in {path.name}")

            X_chunk = frame.to_numpy(dtype=np.float32)
            source_rows += len(y_chunk)

            source_class_counts[0] += int((y_chunk == 0).sum())
            source_class_counts[1] += int((y_chunk == 1).sum())

            chunk_keys = rng.random(len(y_chunk))

            if len(chunk_keys) > TRAINING_SAMPLE_SIZE:
                candidate_indices = np.argpartition(
                    chunk_keys, 
                    TRAINING_SAMPLE_SIZE - 1,
                    )[:TRAINING_SAMPLE_SIZE]
            else:
                candidate_indices = np.arange(len(chunk_keys))
            
            candidate_keys = chunk_keys[candidate_indices]
            candidate_X = X_chunk[candidate_indices]
            candidate_y = y_chunk[candidate_indices]

            combined_keys = np.concatenate(
                (sample_keys, candidate_keys)
            )
            combined_X = np.concatenate(
                (sample_X, candidate_X), 
                axis=0,
            )
            combined_y = np.concatenate(
                (sample_y, candidate_y)
            )

            keep_count = min(
                TRAINING_SAMPLE_SIZE, 
                len(combined_keys),
            )

            if len(combined_keys) > keep_count:
                keep = np.argpartition(
                    combined_keys, 
                    keep_count - 1,
                )[:keep_count]
            else:
                keep = np.arange(len(combined_keys))

            sample_keys = combined_keys[keep]
            sample_X = combined_X[keep]
            sample_y = combined_y[keep]

            del(
                X_chunk,
                Y_chunk,
                chunk_keys,
                candidate_keys,
                candidate_X,
                candidate_y,
                combined_keys,
                combined_X,
                combined_y,
                keep,
            )
            

    if len(sample_y) != TRAINING_SAMPLE_SIZE:
        raise ValueError(
            f"Expected {TRAINING_SAMPLE_SIZE} sampled rows; "
            f"got {len(sample_y)}."
        )

    sample_class_counts = {
        "BENIGN": int((sample_y == 0).sum()),
        "ATTACK": int((sample_y == 1).sum()),
    }

    print("\nTraining sample")
    print(f"Eligible source rows: {source_rows:,}")
    print(f"Sample rows: {len(sample_y):,}")
    print(f"Features: {sample_X.shape[1]}")
    print(f"BENIGN: {sample_class_counts['BENIGN']:,}")
    print(f"ATTACK: {sample_class_counts['ATTACK']:,}")

    model = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            (
                "classifier",
                RandomForestClassifier(
                    n_estimators=100,
                    max_depth=20,
                    min_samples_leaf=2,
                    random_state=RANDOM_STATE,
                    n_jobs=2,
                    class_weight=None,
                ),
            ),
        ]
    )

    print("\nFitting Random Forest...")
    model.fit(sample_X, sample_y)

    del sample_X, sample_y, sample_keys

    # Evaluate the entire held-out capture in chunks.
    total_confusion = np.zeros((2, 2), dtype=np.int64)
    test_rows = 0
    test_class_counts = {0: 0, 1: 0}

    print(f"\nEvaluating held-out capture: {HELD_OUT_CAPTURE}")

    for frame, y_chunk in iter_csv_chunks(held_out_path):
        if frame.columns.tolist() != expected_features:
            raise ValueError("Held-out feature schema mismatch.")

        X_chunk = frame.to_numpy(dtype=np.float32)
        predictions = model.predict(X_chunk)

        total_confusion += confusion_matrix(
            y_chunk, predictions, labels=[0, 1]
        )

        test_rows += len(y_chunk)
        test_class_counts[0] += int((y_chunk == 0).sum())
        test_class_counts[1] += int((y_chunk == 1).sum())

    tn, fp = total_confusion[0]
    fn, tp = total_confusion[1]

    # Construct aggregate class metrics from the accumulated confusion matrix.
    y_true_aggregate = np.repeat(
        [0, 0, 1, 1],
        [int(tn), int(fp), int(fn), int(tp)],
    )
    y_pred_aggregate = np.repeat(
        [0, 1, 0, 1],
        [int(tn), int(fp), int(fn), int(tp)],
    )

    accuracy = float((tn + tp) / test_rows)

    report = {
        "experiment": "Thursday WebAttacks capture holdout",
        "held_out_capture": HELD_OUT_CAPTURE,
        "training_captures": TRAINING_CAPTURES,
        "random_seed": RANDOM_STATE,
        "sampling_method": (
            "Key-based uniform sample of 300,000 rows from eligible "
            "Monday-Thursday captures, excluding the held-out capture"
        ),
        "eligible_source_rows": source_rows,
        "eligible_source_class_counts": {
            "BENIGN": source_class_counts[0],
            "ATTACK": source_class_counts[1],
        },
        "training_sample_rows": TRAINING_SAMPLE_SIZE,
        "training_sample_class_counts": sample_class_counts,
        "features": len(expected_features),
        "feature_names": expected_features,
        "test_rows": test_rows,
        "test_class_counts": {
            "BENIGN": test_class_counts[0],
            "ATTACK": test_class_counts[1],
        },
        "model": {
            "type": "RandomForestClassifier",
            "n_estimators": 100,
            "max_depth": 20,
            "min_samples_leaf": 2,
            "n_jobs": 2,
            "class_weight": None,
        },
        "imputation": "median; fitted on training sample only",
        "confusion_matrix_labels": ["BENIGN", "ATTACK"],
        "confusion_matrix": total_confusion.tolist(),
        "accuracy": accuracy,
        "false_positives": int(fp),
        "false_negatives": int(fn),
        "classification_report": classification_report(
            y_true_aggregate,
            y_pred_aggregate,
            labels=[0, 1],
            target_names=["BENIGN", "ATTACK"],
            output_dict=True,
            zero_division=0,
        ),
        "scikit_learn_version": sklearn.__version__,
        "elapsed_seconds": round(time.time() - started, 2),
        "limitations": [
            "Training uses a 300,000-row sample, not every eligible row.",
            "Only one held-out capture is evaluated.",
            "The held-out web-attack families are absent from training.",
            "SQL Injection has only 21 test records.",
            "Binary classification does not identify attack families.",
            "CIC-IDS2017 results do not establish production effectiveness.",
        ],
    }

    joblib.dump(model, MODEL_PATH)

    with REPORT_PATH.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=2)

    print("\nHoldout evaluation results")
    print(f"Test rows: {test_rows:,}")
    print("Confusion matrix (actual rows, predicted columns):")
    print(total_confusion)
    print(f"Accuracy: {accuracy:.4f}")
    print(f"False positives: {fp:,}")
    print(f"False negatives: {fn:,}")

    print("\nPer-class metrics:")
    for label in ("BENIGN", "ATTACK"):
        metrics = report["classification_report"][label]
        print(
            f"{label}: "
            f"precision={metrics['precision']:.4f}, "
            f"recall={metrics['recall']:.4f}, "
            f"F1={metrics['f1-score']:.4f}"
        )

    print(f"\nSaved model: {MODEL_PATH}")
    print(f"Saved report: {REPORT_PATH}")
    print(f"Elapsed time: {report['elapsed_seconds']:.2f}s")


if __name__ == "__main__":
    main()
