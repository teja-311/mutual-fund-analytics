import pandas as pd
import matplotlib.pyplot as plt

perf = pd.read_csv("data/processed/clean_scheme_performance.csv")

top5 = (
    perf.sort_values(
        "return_3yr_pct",
        ascending=False
    )
    .head(5)
)

plt.figure(figsize=(10,6))

plt.bar(
    top5["scheme_name"],
    top5["return_3yr_pct"]
)

plt.xticks(rotation=45, ha="right")
plt.title("Top 5 Funds by 3-Year Return")
plt.ylabel("3-Year Return (%)")

plt.tight_layout()

plt.savefig("charts/top5_fund_returns.png")
plt.show()

print(
    top5[
        ["scheme_name",
         "return_3yr_pct",
         "benchmark_3yr_pct"]
    ]
)