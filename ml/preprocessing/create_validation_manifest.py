
import json
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

PROJECT_ROOT = Path(__file__).resolve().parents[2]
PROCESSED_DIR = PROJECT_ROOT / "data" / "cicids2017" / "processed"
OUTPUT_PATH = PROCESSED_DIR / "binary_validation_manifest.json"

TRAINING_SOURCE_FILES = [
    "cleaned_Monday-WorkingHours.pcap_ISCX.csv",
    "cleaned_Tuesday-WorkingHours.pcap_ISCX.csv",
    "cleaned_Wednesday-workingHours.pcap_ISCX.csv",
    "cleaned_Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv",
    "cleaned_Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv",
]

CHUNK_SIZE = 100_000
VALIDATION_FRACTION = 0.20
RANDOM_SEED = 42


def main():
    rng = np.random.default_rng(RANDOM_SEED)
    sampled_keys = np.empty(0, dtype=np.float64)
    sampled_labels = np.empty(0, dtype=np.int8)
    total_rows = 0
    source_counts = Counter()
    file_counts = {}

    print("Scanning Monday–Thursday source captures...")

    for filename in TRAINING_SOURCE_FILES:
        path = PROCESSED_DIR / filename

        if not path.is_file():
            raise FileNotFoundError(f"Missing processed file: {path}")

        rows = 0
        labels_count = Counter()

        for chunk in pd.read_csv(
            path,
            usecols=["Label"],
            dtype={"Label": "string"},
            chunksize=CHUNK_SIZE,
        ):
            labels = chunk["Label"].str.strip()

            if labels.isna().any():
                raise ValueError(f"Missing labels found in {filename}")

            mapped = (labels != "BENIGN").to_numpy(dtype=np.int8)
            keys = rng.random(len(mapped))

            sampled_keys = np.concatenate((sampled_keys, keys))
            sampled_labels = np.concatenate((sampled_labels, mapped))

            # Retain a reproducible random sample for the manifest.
            # This bounds memory use and makes the split suitable for
            # the planned baseline-sized validation experiment.
            keep = min(300_000, len(sampled_keys))

            if len(sampled_keys) > keep:
                selected = np.argpartition(sampled_keys, keep - 1)[:keep]
                sampled_keys = sampled_keys[selected]
                sampled_labels = sampled_labels[selected]

            rows += len(chunk)
            total_rows += len(chunk)
            labels_count.update(
                "ATTACK" if value == 1 else "BENIGN"
                for value in mapped
            )

        file_counts[filename] = {
            "rows": rows,
            "binary_labels": dict(labels_count),
        }

        source_counts.update(labels_count)
        print(
            f"  {filename}: {rows:,} rows | "
            f"BENIGN={labels_count['BENIGN']:,}, "
            f"ATTACK={labels_count['ATTACK']:,}"
        )

    if total_rows != 2_127_498:
        raise ValueError(
            f"Expected 2,127,498 source rows; found {total_rows:,}"
        )

    if len(sampled_labels) != min(300_000, total_rows):
        raise RuntimeError("Unexpected sample size.")

    indices = np.arange(len(sampled_labels))

    train_indices, validation_indices = train_test_split(
        indices,
        test_size=VALIDATION_FRACTION,
        random_state=RANDOM_SEED,
        stratify=sampled_labels,
    )

    def summarize(indices):
        counts = Counter(
            "ATTACK" if sampled_labels[i] == 1 else "BENIGN"
            for i in indices
        )
        return {
            "rows": int(len(indices)),
            "binary_labels": dict(counts),
        }

    training = summarize(train_indices)
    validation = summarize(validation_indices)

    if set(train_indices) & set(validation_indices):
        raise RuntimeError("Training and validation overlap.")

    if training["rows"] + validation["rows"] != len(sampled_labels):
        raise RuntimeError("Partition row counts do not add up.")

    manifest = {
        "experiment": "Monday-Thursday sampled binary validation",
        "split_method": "stratified random row split",
        "source_captures": file_counts,
        "source_rows": total_rows,
        "sampled_rows": int(len(sampled_labels)),
        "sampling_method": (
            "reproducible random-key reservoir-style sample "
            "across Monday-Thursday source rows"
        ),
        "sample_seed": RANDOM_SEED,
        "validation_fraction": VALIDATION_FRACTION,
        "split_seed": RANDOM_SEED,
        "training": training,
        "validation": validation,
        "limitations": [
            "The split uses a 300,000-row sample, not all source rows.",
            "Rows from the same capture may appear in both partitions.",
            "This is not an unseen-capture or unseen-attack-family test.",
            "Friday captures are excluded from this validation experiment.",
        ],
    }

    OUTPUT_PATH.write_text(
        json.dumps(manifest, indent=2, sort_keys=True),
        encoding="utf-8",
    )

    print("\n========== VALIDATION MANIFEST ==========")
    print(f"Source rows scanned: {total_rows:,}")
    print(f"Sampled rows: {len(sampled_labels):,}")
    print(f"Training partition: {training}")
    print(f"Validation partition: {validation}")
    print(f"Saved manifest: {OUTPUT_PATH}")
    print("PASS: partitions are disjoint and counts match the sample.")
    print("No model was trained; source CSV files were not modified.")


if __name__ == "__main__":
    main()
