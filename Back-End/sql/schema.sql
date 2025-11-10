-- Defining table for each file.

-- Amazon Sale Report
CREATE TABLE IF NOT EXISTS amazon_sale_report (
    order_id TEXT,
    date DATE,
    amount NUMERIC,
    sku TEXT
);

-- Cloud Warehouse Compersion Chart
CREATE TABLE IF NOT EXISTS cloud_warehouse_comparison (
    shiprocket NUMERIC,
    increff NUMERIC
);

-- Expense IIGF
CREATE TABLE IF NOT EXISTS expense_iigf (
    received_amount NUMERIC,
    expense TEXT
);

-- International Sale Report
CREATE TABLE IF NOT EXISTS international_sale_report (
    date DATE,
    customer TEXT,
    sku TEXT,
    pcs INTEGER,
    rate NUMERIC,
    gross_amt NUMERIC
);

-- May 2022 Pricing
CREATE TABLE IF NOT EXISTS may_2022_pricing (
    sku TEXT,
    style_id TEXT,
    category TEXT,
    tp NUMERIC,
    ajio_mrp NUMERIC
);

-- P&L March 2021
CREATE TABLE IF NOT EXISTS pl_march_2021 (
    sku TEXT,
    style_id TEXT,
    category TEXT,
    tp_1 NUMERIC,
    ajio_mrp NUMERIC
);

-- Sale Report
CREATE TABLE IF NOT EXISTS sale_report (
    sku_code TEXT,
    design_no TEXT,
    stock NUMERIC
);

