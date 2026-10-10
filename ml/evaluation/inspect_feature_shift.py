
from pathlib import Path

import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data" / "cicids2017" / "processed"

TRAIN_FILES = [
    "cleaned_Monday-WorkingHours.pcap_ISCX.csv",
    "cleaned_Tuesday-WorkingHours.pcap_ISCX.csv",
    "cleaned_Wednesday-workingHours.pcap_ISCX.csv",
    "cleaned_Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv",
    "cleaned_Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv",
]

TEST_FILES = [
    "cleaned_Friday-WorkingHours-Morning.pcap_ISCX.csv",
    "cleaned_Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv",
    "cleaned_Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv",
]

FEATURES = [
    "Flow Duration",
    "Total Fwd Packets",
    "Total Backward Packets",
    "Total Length of Fwd Packets",
    "Total Length of Bwd Packets",
    "Fwd Packet Length Max",
    "Fwd Packet Length Mean",
    "Bwd Packet Length Mean",
    "Flow Packets/s",
    "Flow Bytes/s",
    "SYN Flag Count",
    "ACK Flag Count",
    "Init_Win_bytes_forward",
    "Init_Win_bytes_backward",
]

CHUNK_SIZE = 100_000
SAMPLE_PER_FILE = 20_000
RANDOM_SEED = 42


def sample_features(filenames):
    samples = []

    for filename in filenames:
        path = DATA_DIR / filename
        rng = np.random.default_rng(RANDOM_SEED)

        parts = []
        seen = 0

        for chunk in pd.read_csv(
            path,
            usecols=FEATURES,
            chunksize=CHUNK_SIZE,
            low_memory=False,
        ):
            numeric = chunk.apply(pd.to_numeric, errors="coerce")
            numeric = numeric.replace([np.inf, -np.inf], np.nan)

            keys = rng.random(len(numeric))
            parts.append(numeric.assign(_sample_key=keys))
            seen += len(numeric)

        sampled = pd.concat(parts, ignore_index=True)
        sampled = sampled.nsmallest(SAMPLE_PER_FILE, "_sample_key")
        sampled = sampled.drop(columns="_sample_key")

        print(
            f"{filename}: sampled {len(sampled):,} of {seen:,} rows"
        )
        samples.append(sampled)

    return pd.concat(samples, ignore_index=True)


def summarize(name, frame):
    print(f"\n{name}")
    print("-" * len(name))

    summary = frame[FEATURES].agg(["median", "mean", "std"]).T
    summary["missing_count"] = frame[FEATURES].isna().sum()
    summary["infinite_count"] = np.isinf(
        frame[FEATURES].to_numpy(dtype=np.float64)
    ).sum(axis=0)

    print(summary.round(3).to_string())


def main():
    print("Sampling training captures...")
    training = sample_features(TRAIN_FILES)

    print("\nSampling Friday morning...")
    morning = sample_features([TEST_FILES[0]])

    print("\nSampling Friday DDoS...")
    ddos = sample_features([TEST_FILES[1]])

    print("\nSampling Friday PortScan...")
    portscan = sample_features([TEST_FILES[2]])

    summarize("Monday–Thursday training sample", training)
    summarize("Friday morning sample", morning)
    summarize("Friday DDoS sample", ddos)
    summarize("Friday PortScan sample", portscan)


if __name__ == "__main__":
    main()
