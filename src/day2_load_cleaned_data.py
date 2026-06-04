import pandas as pd
import sqlite3
from pathlib import Path

conn = sqlite3.connect("bluestock_mf_clean.db")
processed_path = Path("data/processed")

files = [
    "clean_nav_history.csv",
    "clean_investor_transactions.csv",
    "clean_scheme_performance.csv"
]

for file in files:
    df = pd.read_csv(processed_path / file)

    table_name = file.replace(".csv", "")

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )

    print(f"Loaded {table_name}")

conn.close()

print("\nDatabase created successfully!")