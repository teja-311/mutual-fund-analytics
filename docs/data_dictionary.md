# Data Dictionary

## clean_nav_history.csv

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | TEXT | Mutual fund scheme code |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |

---

## clean_investor_transactions.csv

| Column | Type | Description |
|----------|----------|----------|
| investor_id | TEXT | Unique investor ID |
| transaction_date | DATE | Transaction date |
| amfi_code | TEXT | Fund code |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | REAL | Transaction amount |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| city_tier | TEXT | T30 / B30 |
| age_group | TEXT | Investor age group |
| gender | TEXT | Investor gender |
| annual_income_lakh | REAL | Annual income |
| payment_mode | TEXT | Payment method |
| kyc_status | TEXT | Verified / Pending |

---

## clean_scheme_performance.csv

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | TEXT | Fund code |
| return_1yr_pct | REAL | 1-year return |
| return_3yr_pct | REAL | 3-year CAGR |
| return_5yr_pct | REAL | 5-year CAGR |
| alpha | REAL | Alpha |
| beta | REAL | Beta |
| sharpe_ratio | REAL | Sharpe ratio |
| sortino_ratio | REAL | Sortino ratio |
| std_dev_ann_pct | REAL | Annualized volatility |
| max_drawdown_pct | REAL | Maximum drawdown |