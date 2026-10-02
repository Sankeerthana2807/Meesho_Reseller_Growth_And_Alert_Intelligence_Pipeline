-- part1_sql/queries.sql
-- ============================================
-- Q1: Monthly revenue by category
-- ============================================
.output part1_sql/output/monthly_category_revenue.csv
SELECT 
    month,
    category,
    ROUND(SUM(quantity * unit_price), 2) AS revenue,
    COUNT(*) AS n_orders
FROM orders
GROUP BY month, category
ORDER BY month, category;

-- ============================================
-- Q2: Region-wise total revenue and order count
-- ============================================
.output part1_sql/output/region_revenue.csv
SELECT 
    r.region,
    ROUND(SUM(o.quantity * o.unit_price), 2) AS total_revenue,
    COUNT(*) AS n_orders
FROM orders o
JOIN resellers r ON o.reseller_id = r.reseller_id
GROUP BY r.region
ORDER BY r.region;

-- ============================================
-- Q3: Top resellers by total spend (> 50000)
-- ============================================
.output part1_sql/output/top_resellers.csv
SELECT 
    r.reseller_id,
    r.reseller_name,
    ROUND(SUM(o.quantity * o.unit_price), 2) AS total_spend
FROM orders o
JOIN resellers r ON o.reseller_id = r.reseller_id
GROUP BY r.reseller_id
HAVING total_spend > 50000
ORDER BY total_spend DESC
LIMIT 5;

-- ============================================
-- Q4a: Resellers who have never placed an order
-- ============================================
.output part1_sql/output/zero_order_resellers.csv
SELECT 
    r.reseller_id,
    r.reseller_name,
    r.region
FROM resellers r
LEFT JOIN orders o ON r.reseller_id = o.reseller_id
WHERE o.order_id IS NULL;

-- Q4b: Demonstrate COUNT(*) vs COUNT(order_id)
.output part1_sql/output/count_demo.csv
SELECT 
    r.reseller_id,
    COUNT(*) AS count_star,
    COUNT(o.order_id) AS count_order_id
FROM resellers r
LEFT JOIN orders o ON r.reseller_id = o.reseller_id
WHERE r.reseller_id = 'RS024'
GROUP BY r.reseller_id;

-- ============================================
-- Q5: Average Order Value (AOV) for June, Delivered orders only
-- ============================================
.output part1_sql/output/june_aov.csv
SELECT 
    ROUND(SUM(quantity * unit_price) * 1.0 / COUNT(*), 2) AS june_aov
FROM orders
WHERE month = 'June' AND status = 'Delivered';



-- Step 1: Install SQLite
-- Go to the official SQLite download page: https://www.sqlite.org/download.html (sqlite.org in Bing)
-- Download the Windows command-line shell (sqlite-tools) ZIP file.
-- Extract it to a folder (e.g., C:\sqlite).
-- Inside that folder, you’ll see sqlite3.exe.


-- cmd
-- sqlite3 data/meesho_reseller.db < part1_sql/queries.sql
 
-- powershell/terminal
-- Get-Content part1_sql/queries.sql | sqlite3 data/meesho_reseller.db