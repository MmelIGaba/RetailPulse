-- CRUD Operations for RetailPulse Backend
-- This file contains basic Create, Read, Update, Delete operations for each table.

-- ===========================================
-- AMAZON SALE REPORT
-- ===========================================

-- CREATE: Insert a new record into amazon_sale_report
INSERT INTO amazon_sale_report (order_id, date, amount, sku)
VALUES (?, ?, ?, ?);

-- READ: Select all records from amazon_sale_report
SELECT * FROM amazon_sale_report;

-- READ: Select a specific record by order_id
SELECT * FROM amazon_sale_report WHERE order_id = ?;

-- UPDATE: Update amount for a specific order_id
UPDATE amazon_sale_report SET amount = ? WHERE order_id = ?;

-- DELETE: Delete a record by order_id
DELETE FROM amazon_sale_report WHERE order_id = ?;

-- ===========================================
-- CLOUD WAREHOUSE COMPARISON
-- ===========================================

-- CREATE: Insert a new comparison record
INSERT INTO cloud_warehouse_comparison (shiprocket, increff)
VALUES (?, ?);

-- READ: Select all comparison records
SELECT * FROM cloud_warehouse_comparison;

-- READ: Select a specific record by id (assuming auto-increment id)
SELECT * FROM cloud_warehouse_comparison WHERE id = ?;

-- UPDATE: Update shiprocket value for a specific id
UPDATE cloud_warehouse_comparison SET shiprocket = ? WHERE id = ?;

-- DELETE: Delete a record by id
DELETE FROM cloud_warehouse_comparison WHERE id = ?;

-- ===========================================
-- EXPENSE IIGF
-- ===========================================

-- CREATE: Insert a new expense record
INSERT INTO expense_iigf (received_amount, expense)
VALUES (?, ?);

-- READ: Select all expense records
SELECT * FROM expense_iigf;

-- READ: Select a specific record by id
SELECT * FROM expense_iigf WHERE id = ?;

-- UPDATE: Update received_amount for a specific id
UPDATE expense_iigf SET received_amount = ? WHERE id = ?;

-- DELETE: Delete a record by id
DELETE FROM expense_iigf WHERE id = ?;

-- ===========================================
-- INTERNATIONAL SALE REPORT
-- ===========================================

-- CREATE: Insert a new international sale record
INSERT INTO international_sale_report (date, customer, sku, pcs, rate, gross_amt)
VALUES (?, ?, ?, ?, ?, ?);

-- READ: Select all international sale records
SELECT * FROM international_sale_report;

-- READ: Select records for a specific customer
SELECT * FROM international_sale_report WHERE customer = ?;

-- UPDATE: Update pcs for a specific record (assuming id)
UPDATE international_sale_report SET pcs = ? WHERE id = ?;

-- DELETE: Delete a record by id
DELETE FROM international_sale_report WHERE id = ?;

-- ===========================================
-- MAY 2022 PRICING
-- ===========================================

-- CREATE: Insert a new pricing record
INSERT INTO may_2022_pricing (sku, style_id, category, tp, ajio_mrp)
VALUES (?, ?, ?, ?, ?);

-- READ: Select all pricing records
SELECT * FROM may_2022_pricing;

-- READ: Select records for a specific sku
SELECT * FROM may_2022_pricing WHERE sku = ?;

-- UPDATE: Update tp for a specific sku
UPDATE may_2022_pricing SET tp = ? WHERE sku = ?;

-- DELETE: Delete a record by sku
DELETE FROM may_2022_pricing WHERE sku = ?;

-- ===========================================
-- P&L MARCH 2021
-- ===========================================

-- CREATE: Insert a new P&L record
INSERT INTO pl_march_2021 (sku, style_id, category, tp_1, ajio_mrp)
VALUES (?, ?, ?, ?, ?);

-- READ: Select all P&L records
SELECT * FROM pl_march_2021;

-- READ: Select records for a specific sku
SELECT * FROM pl_march_2021 WHERE sku = ?;

-- UPDATE: Update tp_1 for a specific sku
UPDATE pl_march_2021 SET tp_1 = ? WHERE sku = ?;

-- DELETE: Delete a record by sku
DELETE FROM pl_march_2021 WHERE sku = ?;

-- ===========================================
-- SALE REPORT
-- ===========================================

-- CREATE: Insert a new sale report record
INSERT INTO sale_report (sku_code, design_no, stock)
VALUES (?, ?, ?);

-- READ: Select all sale report records
SELECT * FROM sale_report;

-- READ: Select records for a specific sku_code
SELECT * FROM sale_report WHERE sku_code = ?;

-- UPDATE: Update stock for a specific sku_code
UPDATE sale_report SET stock = ? WHERE sku_code = ?;

-- DELETE: Delete a record by sku_code
DELETE FROM sale_report WHERE sku_code = ?;
