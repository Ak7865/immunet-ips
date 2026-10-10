import json
from collections import Counter
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
PROCESSED_DIR = PROJECT_ROOT / "data" / "cicids2017" / "processed"
MANIFEST_PATH = PROCESSED_DIR / "binary_split_manifest.json"
CHUNK_SIZE = 100_000

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

EXPECTED_ROWS = {
    "cleaned_Monday-WorkingHours.pcap_ISCX.csv": 529_918,
    "cleaned_Tuesday-WorkingHours.pcap_ISCX.csv": 445_909,
    "cleaned_Wednesday-workingHours.pcap_ISCX.csv": 692_703,
    "cleaned_Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv": 288_602,
    "cleaned_Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv": 170_366,
    "cleaned_Friday-WorkingHours-Morning.pcap_ISCX.csv": 191_033,
    "cleaned_Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv": 225_745,
    "cleaned_Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv": 286_467,
}

EXPECTED_TOTAL_ROWS = 2_830_743


def inspect_files(filenames: list[str]) -> dict:
    total_rows = 0
    binary_counts = Counter()
    source_label_counts = Counter()
    file_results = {}

    for filename in filenames:
        path = PROCESSED_DIR / filename

        if not path.is_file():
            raise FileNotFoundError(f"Missing processed file: {path}")

        file_rows = 0
        file_binary_counts = Counter()
        file_source_counts = Counter()

        for chunk in pd.read_csv(
            path,
            usecols=["Label"],
            dtype={"Label": "string"},
            chunksize=CHUNK_SIZE,
        ):
            labels = chunk["Label"].str.strip()

            if labels.isna().any():
                raise ValueError(f"Missing labels found in {filename}")

            mapped = labels.map(
                lambda label: "BENIGN" if label == "BENIGN" else "ATTACK"
            )

            file_rows += len(chunk)
            file_binary_counts.update(mapped.tolist())
            file_source_counts.update(labels.tolist())

        expected = EXPECTED_ROWS[filename]
        if file_rows != expected:
            raise ValueError(
                f"{filename}: expected {expected:,} rows, found {file_rows:,}"
            )

        binary_counts.update(file_binary_counts)
        source_label_counts.update(file_source_counts)
        total_rows += file_rows

        file_results[filename] = {
            "rows": file_rows,
            "binary_labels": dict(file_binary_counts),
        }

        print(
            f"  {filename}: {file_rows:,} rows | "
            f"BENIGN={file_binary_counts['BENIGN']:,}, "
            f"ATTACK={file_binary_counts['ATTACK']:,}"
        )

    return {
        "files": file_results,
        "rows": total_rows,
        "binary_labels": dict(binary_counts),
        "source_labels": dict(source_label_counts),
    }


def main() -> None:
    if not PROCESSED_DIR.is_dir():
        raise FileNotFoundError(
            f"Processed directory not found: {PROCESSED_DIR}"
        )

    if set(TRAIN_FILES) & set(TEST_FILES):
        raise ValueError("A file cannot belong to both training and test sets.")

    assigned_files = set(TRAIN_FILES) | set(TEST_FILES)
    if assigned_files != set(EXPECTED_ROWS):
        raise ValueError("The split does not assign exactly the eight expected files.")

    print("Inspecting training files...")
    training = inspect_files(TRAIN_FILES)

    print("\nInspecting held-out Friday test files...")
    testing = inspect_files(TEST_FILES)

    combined_rows = training["rows"] + testing["rows"]
    if combined_rows != EXPECTED_TOTAL_ROWS:
        raise ValueError(
            f"Expected {EXPECTED_TOTAL_ROWS:,} total rows; found {combined_rows:,}"
        )

    manifest = {
        "experiment": "Friday-held-out binary classification",
        "target_mapping": {
            "BENIGN": "BENIGN",
            "all_other_non_missing_labels": "ATTACK",
        },
        "split_method": "capture-day holdout; no random row split",
        "training": training,
        "test": testing,
        "total_rows": combined_rows,
        "imputation": "not applied",
        "model_training": "not performed",
    }

    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=2, sort_keys=True),
        encoding="utf-8",
    )

    print("\n========== SPLIT SUMMARY ==========")
    print(f"Training rows: {training['rows']:,}")
    print(f"Training labels: {training['binary_labels']}")
    print(f"Test rows: {testing['rows']:,}")
    print(f"Test labels: {testing['binary_labels']}")
    print(f"Combined rows: {combined_rows:,}")
    print(f"Manifest: {MANIFEST_PATH}")
    print("\nPASS: All source files are assigned exactly once.")
    print("No datasets were copied or modified.")
    print("No imputation or model training was performed.")


if __name__ == "__main__":
    main()