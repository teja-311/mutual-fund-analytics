import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")
print("Original Shape:", df.shape)

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(["amfi_code", "date"])

before = len(df)
df = df.drop_duplicates()
after = len(df)

print("Duplicates removed:", before - after)
df = df[df["nav"] > 0]
print("Final Shape:", df.shape)

df.to_csv(
    "data/processed/clean_nav_history.csv",
    index=False
)

print("clean_nav_history.csv created successfully")