import pandas as pd

df = pd.read_csv(
    "data/processed/clean_scheme_performance.csv"
)

def recommend_funds(risk_level):

    risk_level = risk_level.lower()

    if risk_level == "low":
        target = "Low"

    elif risk_level == "medium":
        target = "Moderate"

    elif risk_level == "high":
        target = "High"

    elif risk_level == "very high":
        target = "Very High"

    else:
        print(
            "Choose: low, medium, high, very high"
        )
        return

    result = df[
        df["risk_grade"] == target
    ]

    result = result.sort_values(
        "sharpe_ratio",
        ascending=False
    )

    print(
        result[
            [
                "scheme_name",
                "fund_house",
                "risk_grade",
                "sharpe_ratio",
                "return_3yr_pct"
            ]
        ].head(5)
    )

recommend_funds("medium")