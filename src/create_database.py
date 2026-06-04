import pandas as pd
import sqlite3
from pathlib import Path

processed_path = Path("data/processed")
conn = sqlite3.connect("bluestock_mf.db")

for file in processed_path.glob("*.csv"):
    table_name = file.stem
    df = pd.read_csv(file)

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )

    print(f"Loaded {table_name}")

conn.close()
print("Database created successfully!")