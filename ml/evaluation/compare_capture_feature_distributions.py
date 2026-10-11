
import json
from pathlib import Path

import numpy as np
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data" / "cicids2017" / "processed"
OUTPUT_PATH = DATA_DIR / "capture_feature_distribution_comparison.json"

TRAINING_CAPTURES = [
    "cleaned_Monday-WorkingHours.pcap_ISCX.csv",
    "cleaned_Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv",
    "cleaned_Tuesday-WorkingHours.pcap_ISCX.csv",
    "cleaned_Wednesday-workingHours.pcap_ISCX.csv",
]

HELD_OUT_CAPTURE = (
    "cleaned_Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv"
)

CHUNK_SIZE = 50_000
RESERVOIR_SIZE = 100_000
RANDOM_STATE = 42
QUANTILES = [0.25, 0.50, 0.75]

FEATURES = [
    "Destination Port",
    "Flow Duration",
    "Total Fwd Packets",
    "Total Backward Packets",
    "Flow Bytes/s",
    "Flow Packets/s",
    "Packet Length Mean",
    "SYN Flag Count",
    "Init_Win_bytes_forward",
    "Idle Mean",
]


def summarize_capture(filename):
    path = DATA_DIR / filename

    if not path.is_file():
        raise FileNotFoundError(f"Capture not found: {path}")

    rng = np.random.default_rng(RANDOM_STATE)

    reservoirs = {
        feature: np.empty(0, dtype=np.float64)
        for feature in FEATURES
    }
    valid_counts = {feature: 0 for feature in FEATURES}
    missing_counts = {feature: 0 for feature in FEATURES}
    total_rows = 0

    print(f"\nScanning: {filename}")

    for chunk in pd.read_csv(
        path,
        usecols=FEATURES,
        chunksize=CHUNK_SIZE,
        low_memory=False,
    ):
        chunk.columns = chunk.columns.str.strip()
        chunk = chunk[FEATURES].apply(pd.to_numeric, errors="coerce")
        chunk = chunk.replace([np.inf, -np.inf], np.nan)

        total_rows += len(chunk)

        for feature in FEATURES:
            series = chunk[feature]
            missing_counts[feature] += int(series.isna().sum())
            valid = series.dropna().to_numpy(dtype=np.float64)

            reservoir = reservoirs[feature]

            for value in valid:
                seen = valid_counts[feature]
                valid_counts[feature] += 1

                if len(reservoir) < RESERVOIR_SIZE:
                    reservoir = np.append(reservoir, value)
                else:
                    # Algorithm R: each observation has equal
                    # probability of remaining in the reservoir.
                    index = rng.integers(0, seen + 1)
                    if index < RESERVOIR_SIZE:
                        reservoir[index] = value

            reservoirs[feature] = reservoir

    feature_results = {}

    for feature in FEATURES:
        sample = reservoirs[feature]
        missing = missing_counts[feature]

        if sample.size:
            q25, median, q75 = np.quantile(sample, QUANTILES)

            feature_results[feature] = {
                "valid_values": valid_counts[feature],
                "missing_values": missing,
                "missing_rate": (
                    missing / total_rows if total_rows else None
                ),
                "reservoir_sample_size": int(sample.size),
                "min_sample": float(np.min(sample)),
                "q25_approx": float(q25),
                "median_approx": float(median),
                "q75_approx": float(q75),
                "max_sample": float(np.max(sample)),
                "mean_sample": float(np.mean(sample)),
                "std_sample": float(np.std(sample)),
            }
        else:
            feature_results[feature] = {
                "valid_values": 0,
                "missing_values": missing,
                "missing_rate": (
                    missing / total_rows if total_rows else None
                ),
                "reservoir_sample_size": 0,
                "min_sample": None,
                "q25_approx": None,
                "median_approx": None,
                "q75_approx": None,
                "max_sample": None,
                "mean_sample": None,
                "std_sample": None,
            }

    print(f"Rows scanned: {total_rows:,}")
    print("Feature summaries calculated.")

    return {
        "capture": filename,
        "rows": total_rows,
        "features": feature_results,
    }

def main():
    capture_names = TRAINING_CAPTURES + [HELD_OUT_CAPTURE]

    for name in capture_names:
        if not (DATA_DIR / name).is_file():
            raise FileNotFoundError(f"Required capture missing: {name}")

    results = {
        name: summarize_capture(name)
        for name in capture_names
    }

    output = {
        "experiment": "Training-versus-held-out feature distribution",
        "training_captures": TRAINING_CAPTURES,
        "held_out_capture": HELD_OUT_CAPTURE,
        "features": FEATURES,
        "quantiles": QUANTILES,
        "sampling": {
            "method": "Reservoir sampling",
            "max_values_per_feature_per_capture": RESERVOIR_SIZE,
            "random_state": RANDOM_STATE,
            "quantiles_are_approximate": True,
        },
        "method": (
            "Chunked CSV reads; numeric coercion; infinities treated "
            "as missing; descriptive summaries computed from bounded "
            "reservoir samples."
        ),
        "limitations": [
            "Quantiles, mean, standard deviation, and sample extrema "
            "are estimated from the reservoir sample.",
            "Distribution differences do not establish causation.",
            "Capture identity and attack-family differences may be confounded.",
            "This is a descriptive analysis, not model retraining.",
        ],
        "captures": results,
    }

    OUTPUT_PATH.write_text(
        json.dumps(output, indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )

    print(f"\nReport saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
