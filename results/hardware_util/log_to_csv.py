import csv
from pathlib import Path

INPUT_DIR = Path("./original/small")
OUTPUT_DIR = Path("./original/small")  # same directory; change if you want

FIELDNAMES = [
    "gpu",
    "sm_pct",
    "mem_pct",
    "enc_pct",
    "dec_pct",
    "jpg_pct",
    "ofa_pct",
    "fb_mb",
    "bar1_mb",
    "ccpm_mb",
]

for log_path in sorted(INPUT_DIR.glob("*.log")):
    csv_path = OUTPUT_DIR / f"{log_path.stem}.csv"

    with open(log_path, "r") as fin, open(csv_path, "w", newline="") as fout:
        writer = csv.DictWriter(fout, fieldnames=FIELDNAMES)
        writer.writeheader()

        for line in fin:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            row_vals = line.split()
            if len(row_vals) != 10:
                continue

            writer.writerow({
                "gpu": row_vals[0],
                "sm_pct": row_vals[1],
                "mem_pct": row_vals[2],
                "enc_pct": row_vals[3],
                "dec_pct": row_vals[4],
                "jpg_pct": row_vals[5],
                "ofa_pct": row_vals[6],
                "fb_mb": row_vals[7],
                "bar1_mb": row_vals[8],
                "ccpm_mb": row_vals[9],
            })

    print(f"Saved: {csv_path}")
