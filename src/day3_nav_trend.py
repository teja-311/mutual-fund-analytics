import pandas as pd
import matplotlib.pyplot as plt

nav = pd.read_csv("data/processed/clean_nav_history.csv")
nav["date"] = pd.to_datetime(nav["date"])
daily_nav = nav.groupby("date")["nav"].mean()

plt.figure(figsize=(12,6))
plt.plot(daily_nav.index, daily_nav.values)

plt.title("Average Daily NAV Trend (2022-2026)")
plt.xlabel("Date")
plt.ylabel("Average NAV")

plt.tight_layout()
plt.savefig("charts/nav_trend.png")
plt.show()