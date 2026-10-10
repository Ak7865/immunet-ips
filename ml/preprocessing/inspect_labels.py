
import csv
from pathlib import Path

import numpy as np
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DIR = (
    PROJECT_ROOT
    / "data"
    / "cicids2017"
    / "raw"
    / "MachineLearningCVE"
)

OUTPUT_DIR = (
    PROJECT_ROOT
    / "data"
    / "cicids2017"
    / "processed"
)

CHUNK_SIZE = 100_000
DUPLICATE_COLUMN_INDEX = 55
LABEL_COLUMN = "Label"

# Explicit mappings for the three affected CIC-IDS2017 labels.
LABEL_REPLACEMENTS = {
    "Web Attack \ufffdBrute Force": "Web Attack Brute Force",
    "Web Attack \ufffdSql Injection": "Web Attack Sql Injection",
    "Web Attack \ufffdXSS": "Web Attack XSS",
}


def normalize_column(name: str) -> str:
    """Trim and collapse whitespace in a column name."""
    return " ".join(name.strip().split())


def get_clean_columns(csv_path: Path) -> tuple[list[str], list[int]]:
    """Read the original header and select columns safely."""
    with csv_path.open(
        "r",
        encoding="utf-8-sig",
        errors="replace",
        newline="",
    ) as file:
        original_header = next(csv.reader(file), None)

    if not original_header:
        raise ValueError(f"Empty CSV file: {csv_path}")

    if DUPLICATE_COLUMN_INDEX >= len(original_header):
        raise ValueError(
            f"Expected duplicate column is missing: {csv_path.name}"
        )

    normalized = [
        normalize_column(name) for name in original_header
    ]

    if normalized[DUPLICATE_COLUMN_INDEX] != "Fwd Header Length":
        raise ValueError(
            f"Unexpected column at index {DUPLICATE_COLUMN_INDEX} "
            f"in {csv_path.name}: "
            f"{normalized[DUPLICATE_COLUMN_INDEX]!r}"
        )

    # The two original Fwd Header Length columns were verified identical.
    keep_indices = [
        index
        for index in range(len(original_header))
        if index != DUPLICATE_COLUMN_INDEX
    ]

    columns = [normalized[index] for index in keep_indices]

    if len(columns) != len(set(columns)):
        raise ValueError(
            f"Duplicate column names remain after normalization: "
            f"{csv_path.name}"
        )

    if sum(name.casefold() == LABEL_COLUMN.casefold() for name in columns) != 1:
        raise ValueError(
            f"Expected exactly one {LABEL_COLUMN} column in "
            f"{csv_path.name}"
        )

    return columns, keep_indices


def clean_chunk(chunk: pd.DataFrame) -> pd.DataFrame:
    """Normalize labels and feature values without imputing them."""
    if LABEL_COLUMN not in chunk.columns:
        raise ValueError(f"Missing {LABEL_COLUMN} column")

    labels = chunk[LABEL_COLUMN].astype("string").str.strip()
    chunk[LABEL_COLUMN] = labels.replace(LABEL_REPLACEMENTS)

    feature_columns = [
        column
        for column in chunk.columns
        if column != LABEL_COLUMN
    ]

    for column in feature_columns:
        chunk[column] = pd.to_numeric(
            chunk[column],
            errors="raise",
        )

    # Infinite values cannot be used directly by the planned baseline.
    chunk[feature_columns] = chunk[feature_columns].replace(
        [np.inf, -np.inf],
        np.nan,
    )

    return chunk


def process_file(csv_path: Path, output_path: Path) -> dict:
    """Clean one CSV in chunks and write its intermediate output."""
    columns, keep_indices = get_clean_columns(csv_path)

    rows_read = 0
    missing_feature_values = 0
    label_counts: dict[str, int] = {}

    first_chunk = True

    for chunk in pd.read_csv(
        csv_path,
        header=0,
        usecols=keep_indices,
        chunksize=CHUNK_SIZE,
        encoding="utf-8-sig",
        encoding_errors="replace",
        low_memory=False,
    ):
        # Assign normalized names in original selected-column order.
        chunk.columns = columns
        chunk = clean_chunk(chunk)

        rows_read += len(chunk)

        feature_columns = [
            column
            for column in chunk.columns
            if column != LABEL_COLUMN
        ]

        missing_feature_values += int(
            chunk[feature_columns].isna().sum().sum()
        )

        counts = chunk[LABEL_COLUMN].value_counts(dropna=False)

        for label, count in counts.items():
            label_name = "<MISSING LABEL>" if pd.isna(label) else str(label)
            label_counts[label_name] = (
                label_counts.get(label_name, 0) + int(count)
            )

        chunk.to_csv(
            output_path,
            mode="w" if first_chunk else "a",
            header=first_chunk,
            index=False,
        )

        first_chunk = False

    return {
        "file": csv_path.name,
        "output": output_path.name,
        "rows_read": rows_read,
        "missing_feature_values": missing_feature_values,
        "labels": label_counts,
    }


def write_report(results: list[dict], report_path: Path) -> None:
    """Write an auditable summary of the preprocessing run."""
    total_rows = sum(result["rows_read"] for result in results)
    total_missing = sum(
        result["missing_feature_values"] for result in results
    )

    with report_path.open("w", encoding="utf-8") as file:
        file.write("CIC-IDS2017 preprocessing report\n")
        file.write("================================\n")
        file.write(f"Files processed: {len(results)}\n")
        file.write(f"Total rows read: {total_rows:,}\n")
        file.write(
            f"Missing feature values after infinity handling: "
            f"{total_missing:,}\n"
        )
        file.write(f"Duplicate column removed: index {DUPLICATE_COLUMN_INDEX}\n")
        file.write(
            "Imputation: not applied in this stage\n"
        )
        file.write(
            "Original raw CSV files were not modified\n\n"
        )

        for result in results:
            file.write(f"File: {result['file']}\n")
            file.write(f"Output: {result['output']}\n")
            file.write(f"Rows: {result['rows_read']:,}\n")
            file.write(
                "Missing feature values: "
                f"{result['missing_feature_values']:,}\n"
            )
            file.write("Labels:\n")

            for label, count in sorted(result["labels"].items()):
                file.write(f"  {label}: {count:,}\n")

            file.write("\n")


def main() -> None:
    if not RAW_DIR.is_dir():
        raise FileNotFoundError(
            f"Dataset directory not found: {RAW_DIR}"
        )

    csv_files = sorted(RAW_DIR.glob("*.csv"))

    if len(csv_files) != 8:
        raise ValueError(
            f"Expected 8 CSV files, found {len(csv_files)} "
            f"in {RAW_DIR}"
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    results = []

    for index, csv_path in enumerate(csv_files, start=1):
        output_path = OUTPUT_DIR / f"cleaned_{csv_path.name}"

        print(f"[{index}/8] Processing {csv_path.name}")

        result = process_file(csv_path, output_path)
        results.append(result)

        print(f"  Rows read: {result['rows_read']:,}")
        print(
            "  Missing feature values: "
            f"{result['missing_feature_values']:,}"
        )
        print(f"  Saved: {output_path.name}")

    report_path = OUTPUT_DIR / "preprocessing_report.txt"
    write_report(results, report_path)

    print("\nPreprocessing stage completed.")
    print(f"Files processed: {len(results)}")
    print(
        "Total rows read: "
        f"{sum(result['rows_read'] for result in results):,}"
    )
    print(f"Report saved: {report_path}")
    print("Median imputation has not been applied yet.")
    print("Original raw CSV files were not modified.")


if __name__ == "__main__":
    main()
