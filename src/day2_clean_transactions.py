import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")
print("Original Shape:", df.shape)

df["transaction_type"] = df["transaction_type"].str.strip().str.title()
df["transaction_date"] = pd.to_datetime(df["transaction_date"])
df = df[df["amount_inr"] > 0]

before = len(df)
df = df.drop_duplicates()
after = len(df)

print("Duplicates removed:", before - after)

print("\nKYC Status Values:")
print(df["kyc_status"].value_counts())

print("\nTransaction Types:")
print(df["transaction_type"].value_counts())
print("\nFinal Shape:", df.shape)

df.to_csv(
    "data/processed/clean_investor_transactions.csv",
    index=False
)

print("\nclean_investor_transactions.csv created successfully")