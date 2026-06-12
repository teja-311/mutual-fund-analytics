import pandas as pd

df = pd.read_csv("data/processed/clean_investor_transactions.csv")
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

first_txn = (
    df.groupby("investor_id")["transaction_date"]
    .min()
    .dt.year
    .reset_index()
)

first_txn.columns = ["investor_id", "cohort_year"]

df = df.merge(
    first_txn,
    on="investor_id",
    how="left"
)

avg_investment = (
    df.groupby("cohort_year")["amount_inr"]
    .mean()
)

total_investment = (
    df.groupby("cohort_year")["amount_inr"]
    .sum()
)

top_fund = (
    df.groupby(["cohort_year", "amfi_code"])
    .size()
    .reset_index(name="count")
)

top_fund = (
    top_fund.sort_values(
        ["cohort_year", "count"],
        ascending=[True, False]
    )
    .groupby("cohort_year")
    .head(1)
)

report = pd.DataFrame({
    "avg_investment": avg_investment,
    "total_investment": total_investment
}).reset_index()

report = report.merge(
    top_fund[["cohort_year", "amfi_code"]],
    on="cohort_year"
)

report.to_csv(
    "reports/cohort_analysis.csv",
    index=False
)

print(report)
print("\ncohort_analysis.csv created successfully")