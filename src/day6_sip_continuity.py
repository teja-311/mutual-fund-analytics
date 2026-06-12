import pandas as pd

df = pd.read_csv("data/processed/clean_investor_transactions.csv")

sip = df[
    df["transaction_type"]
    .str.lower()
    == "sip"
].copy()

continuity = (
    sip.groupby("investor_id")
    .size()
    .reset_index(name="sip_count")
)

continuity["category"] = pd.cut(
    continuity["sip_count"],
    bins=[0, 5, 15, 1000],
    labels=[
        "Low Continuity",
        "Medium Continuity",
        "High Continuity"
    ]
)

summary = (
    continuity["category"]
    .value_counts()
    .reset_index()
)

summary.columns = [
    "continuity_category",
    "investor_count"
]

summary.to_csv(
    "reports/sip_continuity_report.csv",
    index=False
)

print(summary)

print(
    "\nsip_continuity_report.csv created successfully"
)