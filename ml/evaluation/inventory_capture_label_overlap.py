
import json
from pathlib import Path
from collections import Counter

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data" / "cicids2017" / "processed"
OUTPUT_PATH = DATA_DIR / "capture_label_overlap_inventory.json"

CHUNK_SIZE = 50_000

CAPTURE_FILES = [
    "cleaned_Monday-WorkingHours.pcap_ISCX.csv",
    "cleaned_Tuesday-WorkingHours.pcap_ISCX.csv",
    "cleaned_Wednesday-workingHours.pcap_ISCX.csv",
    "cleaned_Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv",
    "cleaned_Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv",
    "cleaned_Friday-WorkingHours-Morning.pcap_ISCX.csv",
    "cleaned_Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv",
    "cleaned_Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv",
]


def main():
    inventory = {}

    for filename in CAPTURE_FILES:
        capture_path = DATA_DIR / filename

        if not capture_path.is_file():
            raise FileNotFoundError(
                f"Required capture not found: {capture_path}"
            )

        label_counts = Counter()
        total_rows = 0

        print(f"\nScanning: {filename}")

        for chunk in pd.read_csv(
            capture_path,
            usecols=["Label"],
            chunksize=CHUNK_SIZE,
            low_memory=False,
        ):
            labels = chunk["Label"].astype("string").str.strip()

            if labels.isna().any():
                raise ValueError(
                    f"Missing labels found in {filename}"
                )

            counts = labels.value_counts(dropna=False)
            label_counts.update(counts.to_dict())
            total_rows += len(chunk)

        if sum(label_counts.values()) != total_rows:
            raise ValueError(
                f"Label count mismatch in {filename}: "
                f"labels={sum(label_counts.values())}, "
                f"rows={total_rows}"
            )

        inventory[filename] = {
            "total_rows": total_rows,
            "label_counts": dict(sorted(label_counts.items())),
            "label_count_sum": sum(label_counts.values()),
            "counts_reconciled": sum(label_counts.values()) == total_rows,
        }

        print(f"  Total rows: {total_rows:,}")
        print(f"  Original labels: {len(label_counts)}")
        print("  Label counts reconcile: YES")

    output = {
        "purpose": (
            "Descriptive inventory of original CIC-IDS2017 labels "
            "across processed captures"
        ),
        "chunk_size": CHUNK_SIZE,
        "capture_count": len(inventory),
        "captures": inventory,
        "limitations": [
            "Label overlap does not establish causal effects on model performance.",
            "Capture-level distribution differences may remain confounded "
            "with attack-family differences.",
        ],
    }

    OUTPUT_PATH.write_text(
        json.dumps(output, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"\nInventory saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
