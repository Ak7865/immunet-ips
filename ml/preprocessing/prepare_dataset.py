
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
OUTPUT_DIR = PROJECT_ROOT / "data" / "cicids2017" / "processed"

CHUNK_SIZE = 100_000
DUPLICATE_COLUMN_INDEX = 55
LABEL_COLUMN = "Label"



LABEL_REPLACEMENTS = {
    "Web Attack \ufffd Brute Force": "Web Attack Brute Force",
    "Web Attack \ufffd Sql Injection": "Web Attack Sql Injection",
    "Web Attack \ufffd XSS": "Web Attack XSS",
}




def normalize_column(name: str) -> str:
    return " ".join(name.strip().split())


def get_clean_columns(csv_path: Path) -> list[str]:
    with csv_path.open(
        "r",
        encoding="utf-8-sig",
        errors="replace",
        newline="",
    ) as file:
        header = next(csv.reader(file), None)

    if not header:
        raise ValueError(f"Empty CSV: {csv_path}")

    if DUPLICATE_COLUMN_INDEX >= len(header):
        raise ValueError(f"Expected duplicate column missing: {csv_path}")

    columns = [normalize_column(name) for name in header]

    if columns[DUPLICATE_COLUMN_INDEX] != "Fwd Header Length":
        raise ValueError(
            f"Unexpected column at index {DUPLICATE_COLUMN_INDEX}: "
            f"{columns[DUPLICATE_COLUMN_INDEX]!r}"
        )

    # Remove the second, verified-identical Fwd Header Length column.
    columns.pop(DUPLICATE_COLUMN_INDEX)

    if len(columns) != len(set(columns)):
        raise ValueError(f"Duplicate columns remain in {csv_path.name}")

    if columns.count(LABEL_COLUMN) != 1:
        raise ValueError(f"Expected one {LABEL_COLUMN} column")

    return columns


def clean_chunk(chunk: pd.DataFrame) -> pd.DataFrame:
    if LABEL_COLUMN not in chunk.columns:
        raise ValueError(f"Missing {LABEL_COLUMN} column")

    labels = chunk[LABEL_COLUMN].astype("string").str.strip()
    chunk[LABEL_COLUMN] = labels.replace(LABEL_REPLACEMENTS)

    feature_columns = [
        column for column in chunk.columns
        if column != LABEL_COLUMN
    ]

    for column in feature_columns:
        chunk[column] = pd.to_numeric(chunk[column], errors="raise")

    chunk[feature_columns] = chunk[feature_columns].replace(
        [np.inf, -np.inf],
        np.nan,
    )

    return chunk


def process_file(csv_path: Path, output_path: Path) -> dict:
    columns = get_clean_columns(csv_path)
    rows_read = 0
    missing_feature_values = 0
    label_counts = {}

    with csv_path.open(
        "r",
        encoding="utf-8-sig",
        errors="replace",
        newline="",
    ) as file:
        original_header = next(csv.reader(file))

    keep_indices = [
    index
        for index in range(len(original_header))
        if index != DUPLICATE_COLUMN_INDEX
    ]

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
        chunk.columns = columns
        chunk = clean_chunk(chunk)

        rows_read += len(chunk)

        features = [
            column for column in chunk.columns
            if column != LABEL_COLUMN
        ]
        missing_feature_values += int(
            chunk[features].isna().sum().sum()
        )

        counts = chunk[LABEL_COLUMN].value_counts()
        for label, count in counts.items():
            label_counts[str(label)] = (
                label_counts.get(str(label), 0) + int(count)
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


def main() -> None:
    if not RAW_DIR.is_dir():
        raise FileNotFoundError(f"Dataset directory not found: {RAW_DIR}")

    files = sorted(RAW_DIR.glob("*.csv"))
    if len(files) != 8:
        raise ValueError(
            f"Expected 8 CSV files, found {len(files)} in {RAW_DIR}"
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    report = []

    for index, csv_path in enumerate(files, start=1):
        output_path = OUTPUT_DIR / f"cleaned_{csv_path.name}"
        print(f"[{index}/{len(files)}] Processing {csv_path.name}")

        result = process_file(csv_path, output_path)
        report.append(result)

        print(f"  Rows: {result['rows_read']:,}")
        print(
            "  Missing feature values after infinity handling: "
            f"{result['missing_feature_values']:,}"
        )
        print(f"  Output: {output_path}")

    report_path = OUTPUT_DIR / "preprocessing_report.txt"
    with report_path.open("w", encoding="utf-8") as file:
        for result in report:
            file.write(f"File: {result['file']}\n")
            file.write(f"Rows: {result['rows_read']}\n")
            file.write(
                "Missing feature values: "
                f"{result['missing_feature_values']}\n"
            )
            file.write("Labels:\n")
            for label, count in sorted(result["labels"].items()):
                file.write(f"  {label}: {count}\n")
            file.write("\n")

    print("\nPreprocessing stage completed.")
    print(f"Report: {report_path}")
    print("Original raw CSV files were not modified.")
    print("Median imputation has NOT been applied yet.")


if __name__ == "__main__":
    main()
