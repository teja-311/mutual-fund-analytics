import pandas as pd
from pathlib import Path

raw_path = Path("data/raw")

for file in raw_path.iterdir():
    try:
        df = pd.read_csv(file)
        print(f"\n{file.name}")
        print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
        print(df.columns.tolist())
    except Exception as e:
        print(f"Error reading {file.name}: {e}")