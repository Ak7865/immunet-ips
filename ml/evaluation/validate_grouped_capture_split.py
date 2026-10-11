
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedGroupKFold

BASE = Path("data/cicids2017/processed")

FILES = [
    "cleaned_Monday-WorkingHours.pcap_ISCX.csv",
    "cleaned_Tuesday-WorkingHours.pcap_ISCX.csv",
    "cleaned_Wednesday-workingHours.pcap_ISCX.csv",
    "cleaned_Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv",
]

N_SPLITS = 5
RANDOM_STATE = 42


def main():
    frames = []

    for filename in FILES:
        path = BASE / filename
        if not path.exists():
            raise FileNotFoundError(f"Missing dataset: {path}")

        frame = pd.read_csv(path, low_memory=False)
        if "Label" not in frame.columns:
            raise ValueError(f"Missing Label column: {path}")

        frame["_capture"] = filename
        frames.append(frame)
        print(f"Loaded {filename}: {len(frame):,} rows")

    data = pd.concat(frames, ignore_index=True)
    del frames

    labels = data["Label"].astype(str).to_numpy()
    features = data.drop(columns=["Label", "_capture"])

    # Convert to numeric values and normalize infinities to missing values.
    features = features.apply(pd.to_numeric, errors="raise")
    values = features.to_numpy(dtype=np.float64, copy=True)
    values[~np.isfinite(values)] = np.nan
    values[values == 0] = 0.0  # Normalize negative zero.

    # Normalize NaN payloads before hashing and comparing rows.
    values[np.isnan(values)] = np.nan


    print("\nBuilding feature-row hashes...")
    feature_frame = pd.DataFrame(values, columns=features.columns)
    hashes = pd.util.hash_pandas_object(
        feature_frame, index=False
    ).to_numpy(dtype=np.uint64)

    del feature_frame, features

    # Sort equal hashes together so each candidate bucket can be processed
    # independently. Hash equality alone never establishes row equality.
    order = np.argsort(hashes, kind="stable")
    sorted_hashes = hashes[order]
    boundaries = np.r_[
        0,
        np.flatnonzero(sorted_hashes[1:] != sorted_hashes[:-1]) + 1,
        len(order),
    ]

    groups = np.empty(len(data), dtype=np.int32)
    next_group = 0

    for start, end in zip(boundaries[:-1], boundaries[1:]):
        indices = order[start:end]

        if len(indices) == 1:
            groups[indices[0]] = next_group
            next_group += 1
            continue

        # Deduplicate actual normalized rows within this hash bucket.
        # NaNs are replaced with a consistent sentinel only for comparison.
        bucket_values = values[indices].copy()
        bucket_values[np.isnan(bucket_values)] = np.inf

        unique_rows, inverse = np.unique(
            bucket_values, axis=0, return_inverse=True
        )

        group_ids = np.arange(
            next_group, next_group + len(unique_rows), dtype=np.int32
        )
        groups[indices] = group_ids[inverse]
        next_group += len(unique_rows)

    del values, hashes, order, sorted_hashes, boundaries


    print("\n=== Dataset summary ===")
    print(f"Total rows: {len(data):,}")
    print(f"Unique feature groups: {next_group:,}")
    print(f"Original attack families: {len(np.unique(labels))}")

    label_counts = pd.Series(labels).value_counts()
    print("\nOriginal label counts:")
    print(label_counts.to_string())

    # Calculate conflicting-label groups once.
    group_label_pairs = pd.DataFrame({
        "group": groups,
        "label": labels,
    }).drop_duplicates()

    labels_per_group = group_label_pairs.groupby("group")["label"].nunique()
    conflicting_groups = set(
        labels_per_group[labels_per_group > 1].index
    )

    print(
        "\nFeature groups with conflicting labels: "
        f"{len(conflicting_groups):,}"
    )

    splitter = StratifiedGroupKFold(
        n_splits=N_SPLITS,
        shuffle=True,
        random_state=RANDOM_STATE,
    )

    dummy_x = np.zeros((len(data), 1), dtype=np.uint8)
    all_classes = set(np.unique(labels))

    for fold, (train_idx, test_idx) in enumerate(
        splitter.split(dummy_x, labels, groups), start=1
    ):
        train_groups = set(np.unique(groups[train_idx]))
        test_groups = set(np.unique(groups[test_idx]))
        overlap = train_groups.intersection(test_groups)

        train_counts = pd.Series(labels[train_idx]).value_counts()
        test_counts = pd.Series(labels[test_idx]).value_counts()

        missing_train = sorted(all_classes - set(train_counts.index))
        missing_test = sorted(all_classes - set(test_counts.index))

        test_conflicts = len(conflicting_groups.intersection(test_groups))

        print(f"\n=== Fold {fold} ===")
        print(
            f"Train rows: {len(train_idx):,} "
            f"({len(train_idx) / len(data):.2%})"
        )
        print(
            f"Test rows: {len(test_idx):,} "
            f"({len(test_idx) / len(data):.2%})"
        )
        print(f"Train groups: {len(train_groups):,}")
        print(f"Test groups: {len(test_groups):,}")
        print(f"Feature-group overlap: {len(overlap)}")
        print(f"Missing training families: {missing_train}")
        print(f"Missing test families: {missing_test}")
        print(f"Conflicting-label groups in test: {test_conflicts:,}")

        print("\nTraining label counts:")
        print(train_counts.to_string())
        print("\nTest label counts:")
        print(test_counts.to_string())

    print("\nValidation complete. No model was trained.")
    print("No source datasets or existing model artifacts were modified.")


if __name__ == "__main__":
    main()
