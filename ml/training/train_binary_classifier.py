
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
PROCESSED_DIR = PROJECT_ROOT / "data" / "cicids2017" / "processed"
MODEL_DIR = PROJECT_ROOT / "ml" / "models"

TRAIN_FILES = [
    "cleaned_Monday-WorkingHours.pcap_ISCX.csv",
    "cleaned_Tuesday-WorkingHours.pcap_ISCX.csv",
    "cleaned_Wednesday-workingHours.pcap_ISCX.csv",
    "cleaned_Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv",
    "cleaned_Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv",
]

TEST_FILES = [
    "cleaned_Friday-WorkingHours-Morning.pcap_ISCX.csv",
    "cleaned_Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv",
    "cleaned_Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv",
]

EXPECTED_FEATURES = 77
CHUNK_SIZE = 100_000
SAMPLE_SIZE = 300_000
RANDOM_SEED = 42
BENIGN = 0
ATTACK = 1


def load_training_sample():
    """Uniformly sample rows across all training files using fixed-size storage."""
    rng = np.random.default_rng(RANDOM_SEED)

    sample_keys = np.empty(0, dtype=np.float64)
    sample_x = np.empty((0, EXPECTED_FEATURES), dtype=np.float32)
    sample_y = np.empty(0, dtype=np.int8)

    total_seen = 0

    for filename in TRAIN_FILES:
        path = PROCESSED_DIR / filename
        if not path.is_file():
            raise FileNotFoundError(f"Training file not found: {path}")

        print(f"Sampling from {filename}")

        for chunk in pd.read_csv(
            path,
            chunksize=CHUNK_SIZE,
            low_memory=False,
        ):
            if "Label" not in chunk.columns:
                raise ValueError(f"Label column missing in {filename}")

            labels = chunk["Label"].astype("string").str.strip()
            if labels.isna().any():
                raise ValueError(f"Missing labels found in {filename}")

            features = chunk.drop(columns=["Label"]).to_numpy(
                dtype=np.float32,
                copy=True,
            )

            if features.shape[1] != EXPECTED_FEATURES:
                raise ValueError(
                    f"{filename}: expected {EXPECTED_FEATURES} features, "
                    f"found {features.shape[1]}"
                )

            y = (labels != "BENIGN").to_numpy(dtype=np.int8)
            keys = rng.random(len(chunk))

            candidate_keys = np.concatenate((sample_keys, keys))
            candidate_x = np.concatenate((sample_x, features), axis=0)
            candidate_y = np.concatenate((sample_y, y))

            keep = min(SAMPLE_SIZE, len(candidate_keys))

            if len(candidate_keys) > keep:
                selected = np.argpartition(candidate_keys, keep - 1)[:keep]
            else:
                selected = np.arange(keep)

            sample_keys = candidate_keys[selected]
            sample_x = candidate_x[selected]
            sample_y = candidate_y[selected]

            total_seen += len(chunk)

        print(f"  Rows read so far: {total_seen:,}")

    if total_seen == 0:
        raise ValueError("No training rows were read.")

    if len(sample_y) != min(SAMPLE_SIZE, total_seen):
        raise RuntimeError("The sampled row count is incorrect.")

    if len(np.unique(sample_y)) != 2:
        raise ValueError("Training sample must contain both BENIGN and ATTACK.")

    print(f"\nTotal training rows scanned: {total_seen:,}")
    print(f"Rows selected for training: {len(sample_y):,}")
    print(
        "Sample class counts:",
        {
            "BENIGN": int((sample_y == BENIGN).sum()),
            "ATTACK": int((sample_y == ATTACK).sum()),
        },
    )

    return sample_x, sample_y


def evaluate_in_chunks(model):
    """Evaluate the complete Friday holdout without loading it all into RAM."""
    y_true_parts = []
    y_pred_parts = []
    total_rows = 0

    for filename in TEST_FILES:
        path = PROCESSED_DIR / filename
        if not path.is_file():
            raise FileNotFoundError(f"Test file not found: {path}")

        print(f"Evaluating {filename}")

        for chunk in pd.read_csv(path, chunksize=CHUNK_SIZE, low_memory=False):
            labels = chunk["Label"].astype("string").str.strip()

            if labels.isna().any():
                raise ValueError(f"Missing labels found in test file {filename}")

            x = chunk.drop(columns=["Label"]).to_numpy(
                dtype=np.float32,
                copy=True,
            )

            if x.shape[1] != EXPECTED_FEATURES:
                raise ValueError(
                    f"{filename}: expected {EXPECTED_FEATURES} features, "
                    f"found {x.shape[1]}"
                )

            y_true = (labels != "BENIGN").to_numpy(dtype=np.int8)
            y_pred = model.predict(x).astype(np.int8)

            y_true_parts.append(y_true)
            y_pred_parts.append(y_pred)
            total_rows += len(chunk)

    y_true = np.concatenate(y_true_parts)
    y_pred = np.concatenate(y_pred_parts)

    if total_rows != 703_245:
        raise ValueError(
            f"Expected 703,245 Friday test rows; found {total_rows:,}"
        )

    matrix = confusion_matrix(y_true, y_pred, labels=[BENIGN, ATTACK])
    report = classification_report(
        y_true,
        y_pred,
        labels=[BENIGN, ATTACK],
        target_names=["BENIGN", "ATTACK"],
        output_dict=True,
        zero_division=0,
    )

    return total_rows, matrix, report


def main():
    start = time.time()
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    print("=== Step 1: Build training sample ===")
    x_train, y_train = load_training_sample()

    print("\n=== Step 2: Fit imputer and Random Forest ===")
    model = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            (
                "classifier",
                RandomForestClassifier(
                    n_estimators=100,
                    max_depth=20,
                    min_samples_leaf=2,
                    random_state=RANDOM_SEED,
                    n_jobs=2,
                    class_weight=None,
                ),
            ),
        ]
    )

    # The imputer is fitted only by model.fit() on the training sample.
    model.fit(x_train, y_train)

    model_path = MODEL_DIR / "binary_random_forest.joblib"
    joblib.dump(model, model_path)
    print(f"Saved model pipeline: {model_path}")

    # Release the largest training arrays before evaluation.
    del x_train, y_train

    print("\n=== Step 3: Evaluate on Friday holdout ===")
    test_rows, matrix, report = evaluate_in_chunks(model)

    print("\nConfusion matrix (rows=actual, columns=predicted):")
    print("                 BENIGN  ATTACK")
    print(f"Actual BENIGN    {matrix[0, 0]:>6}  {matrix[0, 1]:>6}")
    print(f"Actual ATTACK    {matrix[1, 0]:>6}  {matrix[1, 1]:>6}")

    for label in ("BENIGN", "ATTACK", "macro avg", "weighted avg"):
        values = report[label]
        print(
            f"{label:12} "
            f"precision={values['precision']:.4f} "
            f"recall={values['recall']:.4f} "
            f"f1={values['f1-score']:.4f}"
        )

    result = {
        "experiment": "Friday-held-out binary classification baseline",
        "random_seed": RANDOM_SEED,
        "training_sample_size": SAMPLE_SIZE,
        "test_rows": test_rows,
        "features": EXPECTED_FEATURES,
        "training_sampling": "uniform row sample across Monday-Thursday files",
        "imputation": "median; fitted on training sample only",
        "model": {
            "type": "RandomForestClassifier",
            "n_estimators": 100,
            "max_depth": 20,
            "min_samples_leaf": 2,
            "n_jobs": 2,
        },
        "scikit_learn_version": sklearn.__version__,
        "confusion_matrix_labels": ["BENIGN", "ATTACK"],
        "confusion_matrix": matrix.tolist(),
        "classification_report": report,
        "elapsed_seconds": round(time.time() - start, 2),
        "limitations": [
            "Training uses a 300,000-row sample rather than all training rows.",
            "The test set contains Friday traffic only.",
            "Binary classification does not identify specific attack types.",
        ],
    }

    report_path = PROCESSED_DIR / "binary_baseline_report.json"
    report_path.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print(f"\nSaved evaluation report: {report_path}")
    print(f"Elapsed time: {result['elapsed_seconds']:.1f} seconds")
    print("\nBaseline training and evaluation completed.")


if __name__ == "__main__":
    main()
