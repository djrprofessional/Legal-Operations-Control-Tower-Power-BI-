from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parents[1] / "data"

def build_summary_table() -> pd.DataFrame:
    matters = pd.read_csv(BASE / "matters.csv")
    matters["spend_per_day"] = matters["outside_counsel_spend"] / matters["cycle_days"]
    return matters

if __name__ == "__main__":
    print(build_summary_table())
