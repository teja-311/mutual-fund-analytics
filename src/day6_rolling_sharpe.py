import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nav = pd.read_csv("data/processed/clean_nav_history.csv")
nav["date"] = pd.to_datetime(nav["date"])

top_funds = nav["amfi_code"].unique()[:5]

plt.figure(figsize=(12,6))
for fund in top_funds:

    temp = nav[nav["amfi_code"] == fund].copy()

    temp = temp.sort_values("date")

    temp["daily_return"] = temp["nav"].pct_change()

    rolling_mean = temp["daily_return"].rolling(90).mean()

    rolling_std = temp["daily_return"].rolling(90).std()

    sharpe = (rolling_mean / rolling_std) * np.sqrt(252)

    plt.plot(
        temp["date"],
        sharpe,
        label=str(fund)
    )

plt.title("Rolling 90-Day Sharpe Ratio")
plt.xlabel("Date")
plt.ylabel("Sharpe Ratio")
plt.legend()
plt.grid(True)

plt.savefig(
    "reports/rolling_sharpe_chart.png",
    bbox_inches="tight"
)

plt.show()

print("rolling_sharpe_chart.png created successfully")