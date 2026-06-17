# Mutual Fund Analytics Platform

## Project Overview

This project was developed as part of the Bluestock Data Science Internship Capstone Project. The objective is to build an end-to-end Mutual Fund Analytics Platform that performs data ingestion, cleaning, exploratory data analysis (EDA), performance analytics, advanced risk analytics, and interactive dashboard visualization.

The platform enables analysis of mutual fund performance, investor behavior, SIP trends, portfolio concentration, and risk-adjusted returns using Python, SQL, and Power BI.

---

## Problem Statement

Mutual fund investors often struggle to compare schemes, understand risk metrics, track industry trends, and evaluate portfolio performance.

The goal of this project is to:

* Analyze mutual fund industry data.
* Evaluate fund performance and risk metrics.
* Study investor transaction behavior.
* Generate actionable insights.
* Build interactive dashboards for decision-making.

---

## Dataset Description

The project uses 10 datasets:

| Dataset                  | Description                        |
| ------------------------ | ---------------------------------- |
| 01_fund_master           | Fund metadata and AMFI information |
| 02_nav_history           | Historical NAV data                |
| 03_aum_by_fund_house     | Assets Under Management by AMC     |
| 04_monthly_sip_inflows   | Monthly SIP inflows                |
| 05_category_inflows      | Category-wise fund inflows         |
| 06_industry_folio_count  | Industry folio statistics          |
| 07_scheme_performance    | Fund performance metrics           |
| 08_investor_transactions | Investor transaction records       |
| 09_portfolio_holdings    | Portfolio allocation details       |
| 10_benchmark_indices     | Benchmark index performance        |

---

## Technology Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* SQLite
* SQLAlchemy
* Jupyter Notebook
* Power BI
* Git & GitHub

---

## Project Architecture

Raw Data → Data Validation → Data Cleaning → SQLite Database → Exploratory Data Analysis → Performance Analytics → Advanced Analytics → Power BI Dashboard → Final Report

---

## ETL Pipeline

### Extract

* Loaded all source CSV datasets.
* Retrieved live NAV data using MFAPI.

### Transform

* Cleaned missing values.
* Standardized date formats.
* Validated NAV values.
* Removed duplicates.
* Standardized transaction types.

### Load

* Loaded cleaned datasets into SQLite database.
* Created analytical SQL queries.
* Generated reporting datasets.

---

## Exploratory Data Analysis

Key analyses performed:

* NAV trend analysis
* AUM growth analysis
* SIP inflow analysis
* Category inflow analysis
* Investor demographics
* Geographic transaction distribution
* Risk vs Return analysis

---

## Performance Analytics

Implemented:

* CAGR Analysis
* Sharpe Ratio
* Sortino Ratio
* Alpha & Beta
* Maximum Drawdown
* Fund Scorecard Ranking
* Benchmark Comparison

---

## Advanced Analytics

Implemented:

* Historical VaR (95%)
* Conditional VaR (CVaR)
* Rolling 90-Day Sharpe Ratio
* Investor Cohort Analysis
* SIP Continuity Analysis
* Fund Recommendation Engine
* HHI Portfolio Concentration Analysis

---

## Dashboard Overview

Power BI dashboard contains four pages:

### 1. Industry Overview

* Total AUM
* Total SIP Inflows
* Total Folios
* Industry Trends

### 2. Fund Performance

* Risk vs Return Analysis
* Fund Scorecard
* Top Performing Funds

### 3. Investor Analytics

* State-wise Investments
* Gender Distribution
* Age Group Analysis
* Transaction Type Analysis

### 4. SIP & Market Trends

* SIP Growth Trends
* Category Inflows
* Market Participation Analysis

---

## Project Structure

```text
MutualFundAnalytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├──charts/
│
├──docs/
│
├──sql/
│
├── src/
│
├── notebooks/
│
├── dashboard/
│
├── reports/
│
├── requirements.txt
│
└── README.md
```

## Steps to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Analytics Scripts

```bash
python src/day6_var_cvar.py
python src/day6_rolling_sharpe.py
python src/recommender.py
```

### Open Dashboard

Open the Power BI dashboard file:

```text
bluestock_mf_dashboard.pbix
```

---

## Key Results

* Identified high-risk and low-risk mutual fund schemes.
* Generated risk-adjusted performance rankings.
* Analyzed investor behavior and SIP continuity.
* Built recommendation engine based on risk profile.
* Created interactive business dashboards.


