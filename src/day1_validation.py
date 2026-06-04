import pandas as pd

print("=" * 50)
print("FUND MASTER ANALYSIS")
print("=" * 50)
fund = pd.read_csv("data/raw/01_fund_master.csv")

print("\nNumber of Fund Houses:")
print(fund["fund_house"].nunique())

print("\nCategories:")
print(fund["category"].unique())

print("\nRisk Categories:")
print(fund["risk_category"].unique())
print("\n")

print("=" * 50)
print("AMFI CODE VALIDATION")
print("=" * 50)

nav = pd.read_csv("data/raw/02_nav_history.csv")
missing = set(fund["amfi_code"]) - set(nav["amfi_code"])

if len(missing) == 0:
    print("\nAll AMFI codes validated successfully.")
else:
    print("\nMissing codes:")
    print(missing)