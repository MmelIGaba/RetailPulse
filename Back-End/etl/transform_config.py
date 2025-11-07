TRANSFORM_CONFIG = {
    "Amazon Sale Report.csv": {
        "required_columns": ["Order ID", "Date", "Amount", "SKU"],
        "dedup_keys": ["Order ID", "Date", "SKU"]
    },
    "Cloud Warehouse Compersion Chart.csv": {
        "required_columns": ["Shiprocket", "INCREFF"],
        "dedup_keys": ["Shiprocket", "INCREFF"]
    },
    "Expense IIGF.csv": {
        "required_columns": ["Recived Amount", "Expance"],
        "dedup_keys": ["Recived Amount", "Expance"]
    },
    "International sale Report.csv": {
        "required_columns": ["DATE", "CUSTOMER", "PCS", "RATE"],
        "dedup_keys": ["DATE", "CUSTOMER", "SKU"]
    },
    "May-2022.csv": {
        "required_columns": ["Sku", "Style Id", "Category", "TP", "Ajio MRP"],
        "dedup_keys": ["Sku", "Style Id", "Category"]
    },
    "P  L March 2021.csv": {
        "required_columns": ["Sku", "Style Id", "Category", "TP 1", "Ajio MRP"],
        "dedup_keys": ["Sku", "Style Id", "Category"]
    },
    "Sale Report.csv": {
        "required_columns": ["SKU Code", "Design No.", "Stock"],
        "dedup_keys": ["SKU Code", "Design No."]
    }
}
