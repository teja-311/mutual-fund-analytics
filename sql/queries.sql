-- 1
SELECT COUNT(*) FROM 01_fund_master;

-- 2
SELECT COUNT(*) FROM 02_nav_history;

-- 3
SELECT COUNT(*) FROM 08_investor_transactions;

-- 4
SELECT fund_house, COUNT(*) AS funds
FROM 01_fund_master
GROUP BY fund_house;

-- 5
SELECT transaction_type, COUNT(*)
FROM 08_investor_transactions
GROUP BY transaction_type;

-- 6
SELECT state, SUM(amount_inr)
FROM 08_investor_transactions
GROUP BY state;

-- 7
SELECT category, AVG(return_3yr_pct)
FROM 07_scheme_performance
GROUP BY category;

-- 8
SELECT MAX(nav)
FROM 02_nav_history;

-- 9
SELECT MIN(nav)
FROM 02_nav_history;

-- 10
SELECT AVG(expense_ratio_pct)
FROM 07_scheme_performance;