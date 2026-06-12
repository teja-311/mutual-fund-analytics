import pandas as pd

holdings = pd.read_csv(
    "data/raw/09_portfolio_holdings.csv"
)

results = []

for fund, group in holdings.groupby("amfi_code"):

    weights = group["weight_pct"] / 100

    hhi = (weights ** 2).sum()

    results.append(
        [fund, round(hhi, 4)]
    )

report = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "HHI"
    ]
)

report = report.sort_values(
    "HHI",
    ascending=False
)

report.to_csv(
    "reports/hhi_concentration.csv",
    index=False
)

print(report.head())

print(
    "\nhhi_concentration.csv created successfully"
)