import pandas as pd

df = pd.read_csv("data/processed/clean_scheme_performance.csv")

df["return_rank"] = df["return_3yr_pct"].rank(ascending=False)
df["sharpe_rank"] = df["sharpe_ratio"].rank(ascending=False)
df["alpha_rank"] = df["alpha"].rank(ascending=False)

df["expense_rank"] = df["expense_ratio_pct"].rank(ascending=True)
df["drawdown_rank"] = df["max_drawdown_pct"].rank(ascending=True)

df["score"] = (
    0.30 * (41 - df["return_rank"]) +
    0.25 * (41 - df["sharpe_rank"]) +
    0.20 * (41 - df["alpha_rank"]) +
    0.15 * (41 - df["expense_rank"]) +
    0.10 * (41 - df["drawdown_rank"])
)

scorecard = df[
    [
        "scheme_name",
        "fund_house",
        "return_3yr_pct",
        "sharpe_ratio",
        "alpha",
        "expense_ratio_pct",
        "max_drawdown_pct",
        "score"
    ]
]

scorecard = scorecard.sort_values(
    "score",
    ascending=False
)

scorecard.to_csv(
    "reports/fund_scorecard.csv",
    index=False
)

print("fund_scorecard.csv created successfully")
print("\nTop 10 Funds:")
print(scorecard.head(10))