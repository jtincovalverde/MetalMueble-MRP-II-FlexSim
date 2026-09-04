import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "capacity_plan.csv"


def main() -> None:
    rows = []
    with DATA.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            load = float(row["load_hours"])
            capacity = float(row["available_capacity_hours"])
            gap = capacity - load
            utilization = load / capacity * 100
            rows.append((row["work_center"], load, capacity, gap, utilization))

    bottleneck = max(rows, key=lambda item: item[4])

    print(f"{'Work center':<12} {'Load h':>8} {'Capacity h':>11} {'Gap h':>8} {'Util %':>8}")
    for name, load, capacity, gap, utilization in rows:
        print(f"{name:<12} {load:>8.2f} {capacity:>11.2f} {gap:>8.2f} {utilization:>8.2f}")

    print(f"\nHighest utilization / bottleneck: {bottleneck[0]} ({bottleneck[4]:.2f}%)")


if __name__ == "__main__":
    main()
