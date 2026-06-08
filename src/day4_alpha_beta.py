import pandas as pd

df = pd.read_csv("data/processed/clean_scheme_performance.csv")

alpha_beta = df[
    ["scheme_name", "fund_house", "alpha", "beta"]
]

alpha_beta.to_csv(
    "reports/alpha_beta.csv",
    index=False
)

print("alpha_beta.csv created successfully")