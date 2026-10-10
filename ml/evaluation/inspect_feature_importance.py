
from pathlib import Path

import joblib
import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "cicids2017" / "processed"
MODEL_PATH = ROOT / "ml" / "models" / "binary_random_forest.joblib"

TOP_N = 25


def main():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

    header_path = DATA_DIR / "cleaned_Monday-WorkingHours.pcap_ISCX.csv"

    if not header_path.exists():
        raise FileNotFoundError(f"Dataset file not found: {header_path}")

    columns = list(pd.read_csv(header_path, nrows=0).columns)
    feature_names = [column for column in columns if column != "Label"]

    model = joblib.load(MODEL_PATH)
    classifier = model.steps[-1][1]

    if not hasattr(classifier, "feature_importances_"):
        raise TypeError("The classifier does not expose feature_importances_.")

    importances = classifier.feature_importances_

    if len(feature_names) != len(importances):
        raise ValueError(
            f"Feature-name count ({len(feature_names)}) does not match "
            f"importance count ({len(importances)})."
        )

    report = pd.DataFrame(
        {
            "Feature": feature_names,
            "Importance": importances,
        }
    ).sort_values("Importance", ascending=False)

    report["Importance"] = report["Importance"].astype(float)

    print(f"Total features: {len(report)}")
    print(f"\nTOP {TOP_N} FEATURES")
    print("=" * 65)
    print(
        report.head(TOP_N).to_string(
            index=False,
            formatters={"Importance": lambda value: f"{value:.6f}"},
        )
    )

    output_path = DATA_DIR / "binary_feature_importance.csv"
    report.to_csv(output_path, index=False, float_format="%.8f")

    print(f"\nFull report saved to: {output_path}")


if __name__ == "__main__":
    main()
