
from pathlib import Path

import joblib
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "cicids2017" / "processed"
MODEL_PATH = ROOT / "ml" / "models" / "binary_random_forest.joblib"

CAPTURES = [
    "cleaned_Friday-WorkingHours-Morning.pcap_ISCX.csv",
    "cleaned_Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv",
    "cleaned_Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv",
]

CHUNK_SIZE = 50_000
SAMPLE_PER_LABEL = 2_000
RANDOM_SEED = 42


def main():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

    model = joblib.load(MODEL_PATH)

    # The training script used the processed CSV columns in their
    # original order, excluding the target column "Label".



    sample_csv=DATA_DIR / "cleaned_Monday-WorkingHours.pcap_ISCX.csv"

    if not sample_csv.exists():
        raise FileNotFoundError(f"Sample CSV not found: {sample_csv}")
    

    # Use the same input feature names and order as training.
    feature_names = [
        column
        for column in pd.read_csv(sample_csv,nrows=0).columns
        if column != "Label"
    ]
    if len(feature_names) != 77:
        raise ValueError(
            f"Expected 77 features, but found {len(feature_names)}."
        )

    print(f"Loaded {len(feature_names)} feature names from dataset header.")

    rng = np.random.default_rng(RANDOM_SEED)
    sampled_parts = []

    for filename in CAPTURES:
        path = DATA_DIR / filename

        if not path.exists():
            raise FileNotFoundError(f"Dataset file not found: {path}")

        print(f"\nReading {filename}")

        # Keep a bounded sample for each label in this capture.
        samples = {}

        for chunk in pd.read_csv(
            path,
            usecols=feature_names + ["Label"],
            chunksize=CHUNK_SIZE,
            low_memory=False,
        ):
            chunk["Label"] = chunk["Label"].astype(str).str.strip()

            for label, group in chunk.groupby("Label", sort=False):
                features = group[feature_names].apply(
                    pd.to_numeric,
                    errors="coerce",
                )
                features = features.replace(
                    [np.inf, -np.inf],
                    np.nan,
                )
                features["Label"] = label
                features["_priority"] = rng.random(len(features))

                previous = samples.get(label)
                if previous is not None:
                    features = pd.concat(
                        [previous, features],
                        ignore_index=True,
                    )

                samples[label] = (
                    features.nsmallest(
                        SAMPLE_PER_LABEL,
                        "_priority",
                    )
                    .reset_index(drop=True)
                )

        for label, sample in samples.items():
            sample = sample.drop(columns="_priority")
            sample["Capture"] = filename
            sampled_parts.append(sample)

            print(
                f"  {label}: sampled {len(sample):,} rows"
            )

    data = pd.concat(sampled_parts, ignore_index=True)
    labels = data["Label"]
    features = data[feature_names]

    print("\nRunning predictions with the existing model...")
    predictions = model.predict(features)

    # Find the probability column corresponding to ATTACK.
    classifier = model.steps[-1][1]
    classes = list(classifier.classes_)

    if 1 not in classes:
        raise ValueError(
            f"Expected numeric Attack class 1, but found: {classes}"
        )


    attack_column = classes.index(1)
    attack_probabilities = model.predict_proba(features)[
        :, attack_column
    ]

    results = pd.DataFrame(
        {
            "Capture": data["Capture"],
            "True_Label": labels,
            "Predicted_Label": np.where(
                predictions == 1,
                "ATTACK",
                "BENIGN",
            ),
            "Attack_Probability": attack_probabilities,
        }
    )

    print("\nPREDICTION CONFIDENCE BY TRUE LABEL")
    print("=" * 100)

    summary = (
        results.groupby(["Capture", "True_Label"])
        .agg(
            Sample_Count=("Predicted_Label", "size"),
            Predicted_BENIGN=(
                "Predicted_Label",
                lambda values: int((values == "BENIGN").sum()),
            ),
            Predicted_ATTACK=(
                "Predicted_Label",
                lambda values: int((values == "ATTACK").sum()),
            ),
            Median_Attack_Probability=(
                "Attack_Probability",
                "median",
            ),
            P90_Attack_Probability=(
                "Attack_Probability",
                lambda values: values.quantile(0.90),
            ),
            Mean_Attack_Probability=(
                "Attack_Probability",
                "mean",
            ),
        )
        .reset_index()
    )

    for column in [
        "Median_Attack_Probability",
        "P90_Attack_Probability",
        "Mean_Attack_Probability",
    ]:
        summary[column] = summary[column].map(
            lambda value: f"{value:.4f}"
        )

    print(summary.to_string(index=False))

    output_path = DATA_DIR / "prediction_confidence_by_label.csv"
    summary.to_csv(output_path, index=False)

    print(f"\nSummary saved to: {output_path}")
    print(
        "\nDiagnostic only: do not use these Friday results "
        "as an untouched final test after model tuning."
    )


if __name__ == "__main__":
    main()
