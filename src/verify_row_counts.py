import pandas as pd
import sqlite3

conn = sqlite3.connect("bluestock_mf_clean.db")

tables = [
    "clean_nav_history",
    "clean_investor_transactions",
    "clean_scheme_performance"
]

for table in tables:
    csv_file = f"data/processed/{table}.csv"

    csv_rows = len(pd.read_csv(csv_file))

    db_rows = pd.read_sql_query(
        f"SELECT COUNT(*) as count FROM {table}",
        conn
    )["count"][0]

    print(f"\n{table}")
    print(f"CSV Rows: {csv_rows}")
    print(f"DB Rows : {db_rows}")

    if csv_rows == db_rows:
        print("MATCH")
    else:
        print("MISMATCH")

conn.close()