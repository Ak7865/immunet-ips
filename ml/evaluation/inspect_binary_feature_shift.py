
from pathlib import Path

import numpy as np
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data" / "cicids2017" / "processed"

CHUNK_SIZE = 50_000
SAMPLE_PER_BINARY_LABEL_PER_CAPTURE = 2_000
RANDOM_SEED = 42

FEATURES = [
    "Flow Duration",
    "Total Fwd Packets",
    "Total Backward Packets",
    "Total Length of Fwd Packets",
    "Total Length of Bwd Packets",
    "Fwd Packet Length Mean",
    "Bwd Packet Length Mean",
    "Flow Packets/s",
    "Flow Bytes/s",
    "SYN Flag Count",
    "ACK Flag Count",
    "Init_Win_bytes_forward",
    "Init_Win_bytes_backward",
]

TRAIN_FILES = [
    "cleaned_Monday-WorkingHours.pcap_ISCX.csv",
    "cleaned_Tuesday-WorkingHours.pcap_ISCX.csv",
    "cleaned_Wednesday-workingHours.pcap_ISCX.csv",
    "cleaned_Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv",
    "cleaned_Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv",
]

FRIDAY_FILES = [
    "cleaned_Friday-WorkingHours-Morning.pcap_ISCX.csv",
    "cleaned_Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv",
    "cleaned_Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv",
]


def sample_capture(filename, dataset_name, rng):
    """Sample each binary class independently within one capture."""
    path = DATA_DIR / filename

    if not path.exists():
        raise FileNotFoundError(f"Dataset file not found: {path}")

    usecols = FEATURES + ["Label"]
    samples = {}
    total_rows = 0

    for chunk in pd.read_csv(
        path,
        usecols=usecols,
        chunksize=CHUNK_SIZE,
        low_memory=False,
    ):
        total_rows += len(chunk)

        original_labels = chunk["Label"].astype(str).str.strip()
        chunk["Binary_Label"] = np.where(
            original_labels.str.upper().eq("BENIGN"),
            "BENIGN",
            "ATTACK",
        )

        for binary_label, group in chunk.groupby(
            "Binary_Label",
            sort=False,
        ):
            numeric = group[FEATURES].apply(
                pd.to_numeric,
                errors="coerce",
            )
            numeric = numeric.replace([np.inf, -np.inf], np.nan)
            numeric["_priority"] = rng.random(len(numeric))

            previous = samples.get(binary_label)
            if previous is not None:
                numeric = pd.concat(
                    [previous, numeric],
                    ignore_index=True,
                )

            samples[binary_label] = (
                numeric.nsmallest(
                    SAMPLE_PER_BINARY_LABEL_PER_CAPTURE,
                    "_priority",
                )
                .reset_index(drop=True)
            )

    results = []

    for binary_label, sample in samples.items():
        sample = sample.drop(columns="_priority")
        sample["Binary_Label"] = binary_label
        sample["Dataset"] = dataset_name
        sample["Capture"] = filename
        results.append(sample)

        print(
            f"  {binary_label}: sampled {len(sample):,} "
            f"records from this capture"
        )

    print(f"  Total capture rows: {total_rows:,}")

    if not results:
        return pd.DataFrame(
            columns=FEATURES + ["Binary_Label", "Dataset", "Capture"]
        )

    return pd.concat(results, ignore_index=True)


def main():
    rng = np.random.default_rng(RANDOM_SEED)
    sampled_groups = []

    for dataset_name, filenames in [
        ("Mon-Thu training", TRAIN_FILES),
        ("Friday diagnostic", FRIDAY_FILES),
    ]:
        print(f"\nSampling {dataset_name} captures...")

        for filename in filenames:
            print(f"\n{filename}")
            sampled_groups.append(
                sample_capture(filename, dataset_name, rng)
            )

    combined = pd.concat(sampled_groups, ignore_index=True)

    output_path = DATA_DIR / "binary_feature_shift_by_label.csv"
    report_rows = []

    for (dataset, binary_label), group in combined.groupby(
        ["Dataset", "Binary_Label"],
        sort=True,
    ):
        for feature in FEATURES:
            values = pd.to_numeric(group[feature], errors="coerce")

            report_rows.append(
                {
                    "Dataset": dataset,
                    "Binary_Label": binary_label,
                    "Feature": feature,
                    "Sample_Count": len(group),
                    "Missing_Count": int(values.isna().sum()),
                    "Median": values.median(),
                    "Mean": values.mean(),
                    "Std": values.std(),
                }
            )

    report = pd.DataFrame(report_rows)
    report.to_csv(output_path, index=False, float_format="%.6g")

    print("\n=== BINARY SAMPLE COUNTS ===")
    print(
        combined.groupby(["Dataset", "Binary_Label"])
        .size()
        .to_string()
    )

    print("\n=== FEATURE DISTRIBUTION SUMMARY ===")
    selected_features = [
        "Destination Port",
        "Flow Duration",
        "Flow Packets/s",
        "Init_Win_bytes_forward",
    ]

    # Destination Port is not in FEATURES, so it is intentionally
    # excluded from the summary unless added to FEATURES later.
    selected_features = [
        feature for feature in selected_features
        if feature in FEATURES
    ]

    selected = report[report["Feature"].isin(selected_features)]

    if selected.empty:
        print("No selected summary features are available.")
    else:
        print(
            selected[
                [
                    "Dataset",
                    "Binary_Label",
                    "Feature",
                    "Sample_Count",
                    "Missing_Count",
                    "Median",
                    "Mean",
                ]
            ].to_string(index=False)
        )

    print(f"\nReport saved to: {output_path}")
    print(
        "\nImportant: Friday is diagnostic data, not an untouched "
        "final test set. Binary ATTACK combines different attack families."
    )


if __name__ == "__main__":
    main()
