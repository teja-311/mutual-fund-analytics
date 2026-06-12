import pandas as pd
import numpy as np

nav = pd.read_csv("data/processed/clean_nav_history.csv")
nav["date"] = pd.to_datetime(nav["date"])
nav = nav.sort_values(["amfi_code", "date"])

nav["daily_return"] = nav.groupby("amfi_code")["nav"].pct_change()

nav = nav.dropna()
results = []

for fund, group in nav.groupby("amfi_code"):

    returns = group["daily_return"]

    var_95 = np.percentile(returns, 5)

    cvar_95 = returns[returns <= var_95].mean()

    results.append([
        fund,
        round(var_95 * 100, 4),
        round(cvar_95 * 100, 4)
    ])

report = pd.DataFrame(
    results,
    columns=["amfi_code", "VaR_95_pct", "CVaR_95_pct"]
)

report = report.sort_values("VaR_95_pct")
report.to_csv(
    "reports/var_cvar_report.csv",
    index=False
)

print(report.head(10))
print("\nvar_cvar_report.csv created successfully")