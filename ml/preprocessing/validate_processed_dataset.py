
from pathlib import Path

import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
PROCESSED_DIR = PROJECT_ROOT / "data" / "cicids2017" / "processed"
CHUNK_SIZE = 100_000

EXPECTED_ROWS = {
    "cleaned_Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv": 225_745,
    "cleaned_Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv": 286_467,
    "cleaned_Friday-WorkingHours-Morning.pcap_ISCX.csv": 191_033,
    "cleaned_Monday-WorkingHours.pcap_ISCX.csv": 529_918,
    "cleaned_Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv": 288_602,
    "cleaned_Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv": 170_366,
    "cleaned_Tuesday-WorkingHours.pcap_ISCX.csv": 445_909,
    "cleaned_Wednesday-workingHours.pcap_ISCX.csv": 692_703,
}


def validate_file(path: Path, expected_rows: int) -> dict:
    rows = 0
    missing_features = 0
    infinite_values = 0
    missing_labels = 0
    replacement_character_labels = 0
    label_counts = {}

    header = pd.read_csv(path, nrows=0).columns.tolist()

    if len(header) != 78:
        raise ValueError(
            f"{path.name}: expected 78 columns, found {len(header)}"
        )

    if header.count("Label") != 1:
        raise ValueError(f"{path.name}: expected exactly one Label column")

    feature_columns = [column for column in header if column != "Label"]

    for chunk in pd.read_csv(
        path,
        chunksize=CHUNK_SIZE,
        low_memory=False,
    ):
        rows += len(chunk)

        labels = chunk["Label"].astype("string")
        missing_labels += int(labels.isna().sum())

        replacement_character_labels += int(
            labels.str.contains("\ufffd", regex=False, na=False).sum()
        )

        counts = labels.value_counts(dropna=False)
        for label, count in counts.items():
            label_name = "<MISSING LABEL>" if pd.isna(label) else str(label)
            label_counts[label_name] = (
                label_counts.get(label_name, 0) + int(count)
            )

        features = chunk[feature_columns].to_numpy(dtype=np.float64)
        missing_features += int(np.isnan(features).sum())
        infinite_values += int(np.isinf(features).sum())

    if rows != expected_rows:
        raise ValueError(
            f"{path.name}: expected {expected_rows:,} rows, found {rows:,}"
        )

    return {
        "file": path.name,
        "rows": rows,
        "columns": len(header),
        "missing_features": missing_features,
        "infinite_values": infinite_values,
        "missing_labels": missing_labels,
        "replacement_labels": replacement_character_labels,
        "labels": label_counts,
    }


def main() -> None:
    if not PROCESSED_DIR.is_dir():
        raise FileNotFoundError(
            f"Processed dataset directory not found: {PROCESSED_DIR}"
        )

    actual_files = {path.name for path in PROCESSED_DIR.glob("cleaned_*.csv")}
    expected_files = set(EXPECTED_ROWS)

    if actual_files != expected_files:
        raise ValueError(
            f"Processed CSV file mismatch.\n"
            f"Missing: {sorted(expected_files - actual_files)}\n"
            f"Unexpected: {sorted(actual_files - expected_files)}"
        )

    total_rows = 0
    total_missing = 0
    total_infinite = 0
    total_missing_labels = 0
    total_replacement_labels = 0

    for filename, expected_rows in EXPECTED_ROWS.items():
        path = PROCESSED_DIR / filename
        print(f"\nValidating: {filename}")

        result = validate_file(path, expected_rows)

        print(f"  Rows: {result['rows']:,}")
        print(f"  Columns: {result['columns']}")
        print(f"  Missing feature values: {result['missing_features']:,}")
        print(f"  Infinite feature values: {result['infinite_values']:,}")
        print(f"  Missing labels: {result['missing_labels']:,}")
        print(
            "  Labels containing replacement character: "
            f"{result['replacement_labels']:,}"
        )
        print("  Label distribution:")
        for label, count in sorted(result["labels"].items()):
            print(f"    {label}: {count:,}")

        total_rows += result["rows"]
        total_missing += result["missing_features"]
        total_infinite += result["infinite_values"]
        total_missing_labels += result["missing_labels"]
        total_replacement_labels += result["replacement_labels"]

    print("\n========== VALIDATION SUMMARY ==========")
    print(f"Files validated: {len(EXPECTED_ROWS)}")
    print(f"Total rows: {total_rows:,}")
    print(f"Total missing feature values: {total_missing:,}")
    print(f"Total infinite feature values: {total_infinite:,}")
    print(f"Total missing labels: {total_missing_labels:,}")
    print(
        "Total labels containing replacement character: "
        f"{total_replacement_labels:,}"
    )

    if total_rows != 2_830_743:
        raise ValueError("Overall row count does not match the audited dataset.")

    if total_infinite != 0:
        raise ValueError("Infinite feature values remain in the processed data.")

    if total_missing_labels != 0:
        raise ValueError("Missing labels remain in the processed data.")

    if total_replacement_labels != 0:
        raise ValueError("Unnormalized replacement characters remain in labels.")

    print("\nPASS: Structural and label validation checks succeeded.")
    print("Note: Missing feature values remain and are not imputed yet.")


if __name__ == "__main__":
    main()
