
import csv
from collections import Counter, defaultdict
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
    return " ".join(name.strip().split())


def main() -> None:
    csv_files = sorted(DATASET_DIR.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(
            f"No CSV files found in {DATASET_DIR}"
        )

    for csv_path in csv_files:
        print(f"\n{'=' * 72}")
        print(f"File: {csv_path.name}")

        with csv_path.open(
            "r",
            encoding="utf-8-sig",
            errors="replace",
            newline="",
        ) as file:
            reader = csv.reader(file)
            header = next(reader, None)

            if header is None:
                print("Empty file.")
                continue

            grouped_columns = defaultdict(list)

            for index, raw_name in enumerate(header):
                normalized = normalize_column(raw_name)
                grouped_columns[normalized].append(
                    (index, raw_name)
                )

            duplicates = {
                name: entries
                for name, entries in grouped_columns.items()
                if len(entries) > 1
            }

            print("\nDuplicate columns after normalization:")

            if not duplicates:
                print("  None")
            else:
                for name, entries in duplicates.items():
                    print(f"  Normalized name: {name!r}")
                    for index, raw_name in entries:
                        print(
                            f"    index={index}, "
                            f"original={raw_name!r}"
                        )

        label_counts = Counter()

        with csv_path.open(
            "r",
            encoding="utf-8-sig",
            errors="replace",
            newline="",
        ) as file:
            reader = csv.DictReader(file)

            for row in reader:
                label = row.get("Label")
                if label is not None:
                    label_counts[label.strip()] += 1

        print("\nLabels containing non-ASCII characters:")

        found_non_ascii = False

        for label in sorted(label_counts):
            if any(ord(character) > 127 for character in label):
                found_non_ascii = True
                codepoints = " ".join(
                    f"U+{ord(character):04X}"
                    for character in label
                    if ord(character) > 127
                )
                print(
                    f"  {label!r}: "
                    f"{label_counts[label]:,} rows; "
                    f"non-ASCII={codepoints}"
                )

        if not found_non_ascii:
            print("  None")

    print(f"\n{'=' * 72}")
    print("Header and label inspection completed.")


if __name__ == "__main__":
    main()
