
import csv
from collections import Counter
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATASET_DIR = (
    PROJECT_ROOT
    / "data"
    / "cicids2017"
    / "raw"
    / "MachineLearningCVE"
)


def normalize_column(name: str) -> str:
    """Trim leading/trailing whitespace and collapse repeated spaces."""
    return " ".join(name.strip().split())


def audit_csv(csv_path: Path) -> None:
    print(f"\n{'=' * 72}")
    print(f"File: {csv_path.name}")

    row_count = 0
    malformed_rows = 0
    label_counts = Counter()
    expected_width = None
    normalized_columns = []
    missing_label_rows = 0

    with csv_path.open(
        "r",
        encoding="utf-8-sig",
        errors="replace",
        newline="",
    ) as file:
        reader = csv.reader(file)

        try:
            header = next(reader)
        except StopIteration:
            print("ERROR: Empty CSV file.")
            return

        expected_width = len(header)
        normalized_columns = [
            normalize_column(column) for column in header
        ]

        duplicate_columns = [
            name
            for name, count in Counter(normalized_columns).items()
            if count > 1
        ]

        label_indexes = [
            index
            for index, name in enumerate(normalized_columns)
            if name.casefold() == "label"
        ]

        if len(label_indexes) != 1:
            print(
                "WARNING: Expected exactly one Label column; "
                f"found {len(label_indexes)}."
            )
            label_index = None
        else:
            label_index = label_indexes[0]

        for row in reader:
            if not row:
                continue

            row_count += 1

            if len(row) != expected_width:
                malformed_rows += 1
                continue

            if label_index is not None:
                label = row[label_index].strip()
                if label:
                    label_counts[label] += 1
                else:
                    missing_label_rows += 1

    print(f"Columns: {expected_width}")
    print(f"Data rows: {row_count:,}")
    print(f"Malformed-width rows: {malformed_rows:,}")
    print(f"Rows with missing labels: {missing_label_rows:,}")

    if duplicate_columns:
        print("Duplicate columns after normalization:")
        for name in sorted(set(duplicate_columns)):
            print(f"  - {name}")
    else:
        print("Duplicate columns after normalization: None")

    print("Label counts:")
    if label_counts:
        for label, count in label_counts.most_common():
            print(f"  {label}: {count:,}")
    else:
        print("  No labels counted.")


def main() -> None:
    if not DATASET_DIR.is_dir():
        raise FileNotFoundError(
            f"Dataset directory not found: {DATASET_DIR}"
        )

    csv_files = sorted(DATASET_DIR.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(
            f"No CSV files found in: {DATASET_DIR}"
        )

    print(f"Dataset directory: {DATASET_DIR}")
    print(f"CSV files found: {len(csv_files)}")

    for csv_path in csv_files:
        audit_csv(csv_path)

    print(f"\n{'=' * 72}")
    print("Dataset audit completed.")


if __name__ == "__main__":
    main()
