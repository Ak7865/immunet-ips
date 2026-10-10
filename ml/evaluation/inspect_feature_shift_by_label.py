
from pathlib import Path

import numpy as np
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data" / "cicids2017" / "processed"

CHUNK_SIZE = 50_000
SAMPLE_PER_LABEL_PER_CAPTURE = 2_000
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


def sample_by_label(filename, rng):
    """Keep a bounded random sample for each label in one capture."""
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

        chunk["Label"] = chunk["Label"].astype(str).str.strip()

        for label, group in chunk.groupby("Label", sort=False):
            numeric = group[FEATURES].apply(pd.to_numeric, errors="coerce")
            numeric = numeric.replace([np.inf, -np.inf], np.nan)
            numeric["Label"] = label

            # Random priorities let us retain a representative,
            # bounded sample without storing the entire capture.
            numeric["_priority"] = rng.random(len(numeric))

            previous = samples.get(label)
            if previous is not None:
                numeric = pd.concat(
                    [previous, numeric],
                    ignore_index=True,
                )

            samples[label] = (
                numeric.nsmallest(
                    SAMPLE_PER_LABEL_PER_CAPTURE,
                    "_priority",
                )
                .reset_index(drop=True)
            )

    result = []

    for label, sample in samples.items():
        sample = sample.drop(columns="_priority")
        sample["Capture"] = filename
        result.append(sample)

        print(
            f"  {label}: sampled {len(sample):,} "
            f"of its rows in this capture"
        )

    print(f"  Total capture rows: {total_rows:,}")

    if not result:
        return pd.DataFrame(columns=FEATURES + ["Label", "Capture"])

    return pd.concat(result, ignore_index=True)


def main():
    rng = np.random.default_rng(RANDOM_SEED)

    training_samples = []
    friday_samples = []

    print("Sampling Monday–Thursday training captures...")
    for filename in TRAIN_FILES:
        print(f"\n{filename}")
        training_samples.append(sample_by_label(filename, rng))

    print("\nSampling Friday diagnostic captures...")
    for filename in FRIDAY_FILES:
        print(f"\n{filename}")
        friday_samples.append(sample_by_label(filename, rng))

    training = pd.concat(training_samples, ignore_index=True)
    friday = pd.concat(friday_samples, ignore_index=True)

    # Combine only labels with the same name. For example, this
    # compares training BENIGN with Friday BENIGN, not all traffic.
    training["Dataset"] = "Mon-Thu training"
    friday["Dataset"] = "Friday diagnostic"

    combined = pd.concat([training, friday], ignore_index=True)

    output_dir = DATA_DIR
    output_dir.mkdir(parents=True, exist_ok=True)

    report_path = output_dir / "feature_shift_by_label.csv"
    rows = []

    for (label, dataset), group in combined.groupby(
        ["Label", "Dataset"],
        sort=True,
    ):
        for feature in FEATURES:
            values = pd.to_numeric(
                group[feature],
                errors="coerce",
            )
            rows.append(
                {
                    "Label": label,
                    "Dataset": dataset,
                    "Feature": feature,
                    "Sample_Count": len(group),
                    "Missing_Count": int(values.isna().sum()),
                    "Median": values.median(),
                    "Mean": values.mean(),
                    "Std": values.std(),
                }
            )

    report = pd.DataFrame(rows)
    report.to_csv(report_path, index=False, float_format="%.6g")

    # Print compact summaries for the labels that matter most
    # to the earlier Friday evaluation.
    target_labels = [
        "BENIGN",
        "Bot",
        "DDoS",
        "PortScan",
        "FTP-Patator",
        "SSH-Patator",
        "DoS Hulk",
        "DoS GoldenEye",
        "DoS slowloris",
        "DoS Slowhttptest",
        "Web Attack Brute Force",
        "Web Attack Sql Injection",
        "Web Attack XSS",
        "Infiltration",
        "Heartbleed",
    ]

    selected_features = [
        "Flow Duration",
        "Total Fwd Packets",
        "Total Backward Packets",
        "Flow Packets/s",
        "Flow Bytes/s",
        "SYN Flag Count",
        "ACK Flag Count",
        "Init_Win_bytes_forward",
    ]

    print("\n\nLABEL-AWARE FEATURE COMPARISON")
    print("=" * 90)

    for label in target_labels:
        label_report = report[
            (report["Label"] == label)
            & report["Feature"].isin(selected_features)
        ]

        if label_report.empty:
            continue

        print(f"\nLabel: {label}")
        display = label_report[
            [
                "Dataset",
                "Feature",
                "Sample_Count",
                "Missing_Count",
                "Median",
                "Mean",
            ]
        ].copy()

        for column in ["Median", "Mean"]:
            display[column] = display[column].map(
                lambda value: (
                    f"{value:.6g}" if pd.notna(value) else "NaN"
                )
            )

        print(display.to_string(index=False))

    print(f"\nFull report saved to: {report_path}")
    print(
        "\nImportant: Friday is being used for diagnosis. "
        "Do not treat it as an untouched final test set after this analysis."
    )


if __name__ == "__main__":
    main()
