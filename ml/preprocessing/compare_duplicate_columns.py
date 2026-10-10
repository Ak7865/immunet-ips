
import csv
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATASET_DIR = (
    PROJECT_ROOT
    / "data"
    / "cicids2017"
    / "raw"
    / "MachineLearningCVE"
)

FIRST_INDEX = 34
SECOND_INDEX = 55
MAX_EXAMPLES = 5


def compare_file(csv_path: Path) -> None:
    equal_count = 0
    different_count = 0
    examples = []

    with csv_path.open(
        "r",
        encoding="utf-8-sig",
        errors="replace",
        newline="",
    ) as file:
        reader = csv.reader(file)
        header = next(reader, None)

        if header is None:
            print(f"SKIPPED: Empty file: {csv_path.name}")
            return

        if max(FIRST_INDEX, SECOND_INDEX) >= len(header):
            print(f"ERROR: Missing expected columns in {csv_path.name}")
            return

        for row_number, row in enumerate(reader, start=2):
            if len(row) <= max(FIRST_INDEX, SECOND_INDEX):
                continue

            first_value = row[FIRST_INDEX].strip()
            second_value = row[SECOND_INDEX].strip()

            if first_value == second_value:
                equal_count += 1
            else:
                different_count += 1

                if len(examples) < MAX_EXAMPLES:
                    examples.append(
                        (
                            row_number,
                            first_value,
                            second_value,
                        )
                    )

    print(f"\nFile: {csv_path.name}")
    print(f"Rows with equal values: {equal_count:,}")
    print(f"Rows with different values: {different_count:,}")

    if examples:
        print("First differing examples:")
        for row_number, first_value, second_value in examples:
            print(
                f"  CSV row {row_number}: "
                f"index {FIRST_INDEX}={first_value!r}, "
                f"index {SECOND_INDEX}={second_value!r}"
            )


def main() -> None:
    csv_files = sorted(DATASET_DIR.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(
            f"No CSV files found in {DATASET_DIR}"
        )

    print("Comparing duplicate Fwd Header Length columns.")
    print("Comparison uses the original string values after trimming.")

    for csv_path in csv_files:
        compare_file(csv_path)

    print("\nComparison completed. Original CSV files were not modified.")


if __name__ == "__main__":
    main()
