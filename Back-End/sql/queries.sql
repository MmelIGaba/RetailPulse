-- Analytical Queries for RetailPulse Backend
-- This file contains various analytical queries for each table.

-- ===========================================
-- AMAZON SALE REPORT
-- ===========================================

-- Total sales amount
SELECT SUM(amount) AS total_sales FROM amazon_sale_report;

-- Average sales amount per order
SELECT AVG(amount) AS avg_sales_per_order FROM amazon_sale_report;

-- Top 10 SKUs by total sales amount
SELECT sku, SUM(amount) AS total_amount
FROM amazon_sale_report
GROUP BY sku
ORDER BY total_amount DESC
LIMIT 10;

-- Sales by date (daily totals)
SELECT date, SUM(amount) AS daily_sales
FROM amazon_sale_report
GROUP BY date
ORDER BY date;

-- ===========================================
-- CLOUD WAREHOUSE COMPARISON
-- ===========================================

-- Average shiprocket and increff values
SELECT AVG(shiprocket) AS avg_shiprocket, AVG(increff) AS avg_increff
FROM cloud_warehouse_comparison;

-- Comparison summary (count, min, max)
SELECT
    COUNT(*) AS total_records,
    MIN(shiprocket) AS min_shiprocket,
    MAX(shiprocket) AS max_shiprocket,
    MIN(increff) AS min_increff,
    MAX(increff) AS max_increff
FROM cloud_warehouse_comparison;

-- ===========================================
-- EXPENSE IIGF
-- ===========================================

-- Total received amount
SELECT SUM(received_amount) AS total_received FROM expense_iigf;

-- Expenses grouped by type
SELECT expense, SUM(received_amount) AS total_amount
FROM expense_iigf
GROUP BY expense
ORDER BY total_amount DESC;

-- ===========================================
-- INTERNATIONAL SALE REPORT
-- ===========================================

-- Total gross amount
SELECT SUM(gross_amt) AS total_gross_sales FROM international_sale_report;

-- Sales by customer
SELECT customer, SUM(gross_amt) AS total_sales
FROM international_sale_report
GROUP BY customer
ORDER BY total_sales DESC;

-- Average rate and pcs per sale
SELECT AVG(rate) AS avg_rate, AVG(pcs) AS avg_pcs FROM international_sale_report;

-- Sales by date
SELECT date, SUM(gross_amt) AS daily_gross_sales
FROM international_sale_report
GROUP BY date
ORDER BY date;

-- ===========================================
-- MAY 2022 PRICING
-- ===========================================

-- Average TP and Ajio MRP
SELECT AVG(tp) AS avg_tp, AVG(ajio_mrp) AS avg_ajio_mrp FROM may_2022_pricing;

-- Pricing by category
SELECT category, AVG(tp) AS avg_tp, AVG(ajio_mrp) AS avg_ajio_mrp
FROM may_2022_pricing
GROUP BY category;

-- Top 10 SKUs by TP
SELECT sku, tp
FROM may_2022_pricing
ORDER BY tp DESC
LIMIT 10;

-- ===========================================
-- P&L MARCH 2021
-- ===========================================

-- Average TP 1 and Ajio MRP
SELECT AVG(tp_1) AS avg_tp_1, AVG(ajio_mrp) AS avg_ajio_mrp FROM pl_march_2021;

-- P&L by category
SELECT category, AVG(tp_1) AS avg_tp_1, AVG(ajio_mrp) AS avg_ajio_mrp
FROM pl_march_2021
GROUP BY category;

-- Top 10 SKUs by TP 1
SELECT sku, tp_1
FROM pl_march_2021
ORDER BY tp_1 DESC
LIMIT 10;

-- ===========================================
-- SALE REPORT
-- ===========================================

-- Total stock across all SKUs
SELECT SUM(stock) AS total_stock FROM sale_report;

-- Average stock per SKU
SELECT AVG(stock) AS avg_stock FROM sale_report;

-- Top 10 SKUs by stock
SELECT sku_code, stock
FROM sale_report
ORDER BY stock DESC
LIMIT 10;

-- Stock by design number
SELECT design_no, SUM(stock) AS total_stock
FROM sale_report
GROUP BY design_no
ORDER BY total_stock DESC;
