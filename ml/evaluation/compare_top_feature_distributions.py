
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "cicids2017" / "processed"

IMPORTANCE_PATH = DATA_DIR / "binary_feature_importance.csv"
CHUNK_SIZE = 50_000
SAMPLE_PER_LABEL_PER_CAPTURE = 2_000
RANDOM_SEED = 42

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


def sample_capture(filename, features, rng):
    """Keep a bounded random sample per original label and capture."""
    path = DATA_DIR / filename

    if not path.exists():
        raise FileNotFoundError(f"Dataset file not found: {path}")

    samples = {}

    for chunk in pd.read_csv(
        path,
        usecols=features + ["Label"],
        chunksize=CHUNK_SIZE,
        low_memory=False,
    ):
        chunk["Label"] = chunk["Label"].astype(str).str.strip()

        for label, group in chunk.groupby("Label", sort=False):
            part = group[features].apply(pd.to_numeric, errors="coerce")
            part = part.replace([np.inf, -np.inf], np.nan)
            part["Label"] = label
            part["_priority"] = rng.random(len(part))

            previous = samples.get(label)
            if previous is not None:
                part = pd.concat([previous, part], ignore_index=True)

            samples[label] = (
                part.nsmallest(SAMPLE_PER_LABEL_PER_CAPTURE, "_priority")
                .reset_index(drop=True)
            )

    output = []

    for label, sample in samples.items():
        sample = sample.drop(columns="_priority")
        sample["Capture"] = filename
        output.append(sample)

    if not output:
        return pd.DataFrame(columns=features + ["Label", "Capture"])

    return pd.concat(output, ignore_index=True)


def main():
    if not IMPORTANCE_PATH.exists():
        raise FileNotFoundError(
            f"Feature importance report not found: {IMPORTANCE_PATH}"
        )

    importance = pd.read_csv(IMPORTANCE_PATH)

    if not {"Feature", "Importance"}.issubset(importance.columns):
        raise ValueError(
            "Importance report must contain Feature and Importance columns."
        )

    top_features = (
        importance.sort_values("Importance", ascending=False)
        .head(10)["Feature"]
        .tolist()
    )

    print("Top 10 features selected from the existing model:")
    for rank, feature in enumerate(top_features, start=1):
        print(f"  {rank:2}. {feature}")

    rng = np.random.default_rng(RANDOM_SEED)
    sampled_frames = []

    for dataset_name, filenames in [
        ("Training captures", TRAIN_FILES),
        ("Friday diagnostic captures", FRIDAY_FILES),
    ]:
        print(f"\nSampling {dataset_name}...")

        for filename in filenames:
            print(f"  {filename}")
            sample = sample_capture(filename, top_features, rng)
            sample["Dataset_Group"] = dataset_name
            sampled_frames.append(sample)

    data = pd.concat(sampled_frames, ignore_index=True)

    # Binary grouping matches the original training objective.
    data["Binary_Label"] = np.where(
        data["Label"] == "BENIGN",
        "BENIGN",
        "ATTACK",
    )

    # Report capture-specific results as well as the binary class.
    grouping = ["Dataset_Group", "Capture", "Label", "Binary_Label"]
    rows = []

    for keys, group in data.groupby(grouping, sort=True):
        dataset_group, capture, label, binary_label = keys

        for feature in top_features:
            values = pd.to_numeric(group[feature], errors="coerce")
            finite = values[np.isfinite(values)]

            rows.append(
                {
                    "Dataset_Group": dataset_group,
                    "Capture": capture,
                    "Original_Label": label,
                    "Binary_Label": binary_label,
                    "Feature": feature,
                    "Sample_Count": len(group),
                    "Missing_Count": int(values.isna().sum()),
                    "Q1": finite.quantile(0.25) if len(finite) else np.nan,
                    "Median": finite.median() if len(finite) else np.nan,
                    "Q3": finite.quantile(0.75) if len(finite) else np.nan,
                }
            )

    report = pd.DataFrame(rows)
    output_path = DATA_DIR / "top_feature_distributions.csv"
    report.to_csv(output_path, index=False, float_format="%.8g")

    # Aggregate by binary class and dataset group for an initial comparison.
    aggregate_rows = []

    for (dataset_group, binary_label), group in data.groupby(
        ["Dataset_Group", "Binary_Label"],
        sort=True,
    ):
        for feature in top_features:
            values = pd.to_numeric(group[feature], errors="coerce")
            finite = values[np.isfinite(values)]

            aggregate_rows.append(
                {
                    "Dataset_Group": dataset_group,
                    "Binary_Label": binary_label,
                    "Feature": feature,
                    "Sample_Count": len(group),
                    "Missing_Count": int(values.isna().sum()),
                    "Q1": finite.quantile(0.25) if len(finite) else np.nan,
                    "Median": finite.median() if len(finite) else np.nan,
                    "Q3": finite.quantile(0.75) if len(finite) else np.nan,
                }
            )

    aggregate = pd.DataFrame(aggregate_rows)

    print("\nBINARY-CLASS FEATURE SUMMARY")
    print("=" * 100)

    display = aggregate[
        [
            "Dataset_Group",
            "Binary_Label",
            "Feature",
            "Sample_Count",
            "Missing_Count",
            "Q1",
            "Median",
            "Q3",
        ]
    ].copy()

    for column in ["Q1", "Median", "Q3"]:
        display[column] = display[column].map(
            lambda value: f"{value:.6g}" if pd.notna(value) else "NaN"
        )

    print(display.to_string(index=False))

    print(f"\nCapture-level report: {output_path}")

    aggregate_path = DATA_DIR / "top_feature_distributions_binary.csv"
    aggregate.to_csv(aggregate_path, index=False, float_format="%.8g")
    print(f"Binary summary report: {aggregate_path}")

    print(
        "\nFriday is diagnostic data. These results must not be presented "
        "as untouched final-test evidence."
    )


if __name__ == "__main__":
    main()
