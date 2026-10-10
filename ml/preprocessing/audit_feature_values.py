
import csv
from pathlib import Path

import numpy as np
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATASET_DIR = (
    PROJECT_ROOT
    / "data"
    / "cicids2017"
    / "raw"
    / "MachineLearningCVE"
)

CHUNK_SIZE = 100_000
DUPLICATE_COLUMN_INDEX = 55


def normalize_column(name: str) -> str:
    return " ".join(name.strip().split())


def audit_file(csv_path: Path) -> dict:
    print(f"\nAuditing: {csv_path.name}")

    # Read the raw header first so the duplicate is removed by position,
    # rather than relying on pandas' automatic duplicate-name handling.
    with csv_path.open(
        "r",
        encoding="utf-8-sig",
        errors="replace",
        newline="",
    ) as file:
        header = next(csv.reader(file), None)

    if not header:
        raise ValueError(f"Empty CSV file: {csv_path}")

    if DUPLICATE_COLUMN_INDEX >= len(header):
        raise ValueError(f"Expected duplicate column missing: {csv_path}")

    normalized_header = [
        normalize_column(name) for name in header
    ]

    if normalized_header[DUPLICATE_COLUMN_INDEX] != "Fwd Header Length":
        raise ValueError(
            f"Unexpected column at index {DUPLICATE_COLUMN_INDEX} "
            f"in {csv_path.name}: "
            f"{normalized_header[DUPLICATE_COLUMN_INDEX]!r}"
        )

    keep_indices = [
        index
        for index in range(len(header))
        if index != DUPLICATE_COLUMN_INDEX
    ]

    columns = [normalized_header[index] for index in keep_indices]

    if len(columns) != len(set(columns)):
        raise ValueError(
            f"Other duplicate column names remain in {csv_path.name}"
        )

    label_columns = [
        index
        for index, name in enumerate(columns)
        if name.casefold() == "label"
    ]

    if len(label_columns) != 1:
        raise ValueError(
            f"Expected exactly one Label column in {csv_path.name}"
        )

    label_column = columns[label_columns[0]]
    feature_columns = [
        name for name in columns if name != label_column
    ]

    missing_counts = {name: 0 for name in feature_columns}
    infinite_counts = {name: 0 for name in feature_columns}
    conversion_failures = {name: 0 for name in feature_columns}

    row_count = 0
    label_counts = {}

    # Read by position so the duplicated header cannot cause ambiguity.
    for chunk in pd.read_csv(
        csv_path,
        header=0,
        usecols=keep_indices,
        chunksize=CHUNK_SIZE,
        encoding="utf-8-sig",
        encoding_errors="replace",
        low_memory=False,
    ):
        # Pandas preserves original column order when usecols is a list
        # only in file order; rename using the selected original indexes.
        chunk.columns = columns
        row_count += len(chunk)

        labels = chunk[label_column].astype("string").str.strip()
        for label, count in labels.value_counts(dropna=False).items():
            label_text = "<MISSING LABEL>" if pd.isna(label) else str(label)
            label_counts[label_text] = (
                label_counts.get(label_text, 0) + int(count)
            )

        for name in feature_columns:
            original = chunk[name]
            numeric = pd.to_numeric(original, errors="coerce")

            missing_counts[name] += int(original.isna().sum())

            conversion_failures[name] += int(
                (original.notna() & numeric.isna()).sum()
            )

            numeric_array = numeric.to_numpy(
                dtype="float64",
                na_value=np.nan,
            )
            infinite_counts[name] += int(
                np.isinf(numeric_array).sum()
            )

    print(f"Rows audited: {row_count:,}")
    print(f"Feature columns: {len(feature_columns)}")
    print(f"Labels found: {len(label_counts)}")

    print("\nLabel counts:")
    for label, count in sorted(label_counts.items()):
        print(f"  {label}: {count:,}")

    print("\nFeature columns requiring attention:")
    issue_found = False

    for name in feature_columns:
        missing = missing_counts[name]
        infinite = infinite_counts[name]
        failures = conversion_failures[name]

        if missing or infinite or failures:
            issue_found = True
            print(
                f"  {name}: missing={missing:,}, "
                f"infinite={infinite:,}, "
                f"conversion_failures={failures:,}"
            )

    if not issue_found:
        print("  None found.")

    return {
        "file": csv_path.name,
        "rows": row_count,
        "labels": label_counts,
        "missing": missing_counts,
        "infinite": infinite_counts,
        "conversion_failures": conversion_failures,
    }


def main() -> None:
    csv_files = sorted(DATASET_DIR.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(
            f"No CSV files found in {DATASET_DIR}"
        )

    print(f"CSV files: {len(csv_files)}")
    print(f"Chunk size: {CHUNK_SIZE:,}")
    print("Original CSV files will not be modified.")

    results = [audit_file(path) for path in csv_files]

    print("\n" + "=" * 72)
    print("OVERALL SUMMARY")
    print("=" * 72)
    print(f"Files audited: {len(results)}")
    print(f"Total rows: {sum(result['rows'] for result in results):,}")
    print("Feature-value audit completed.")


if __name__ == "__main__":
    main()
