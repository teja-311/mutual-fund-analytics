import pandas as pd

fund_master = pd.read_excel("data/raw/01_fund_master.xls")

print(fund_master.head())
print(fund_master.shape)