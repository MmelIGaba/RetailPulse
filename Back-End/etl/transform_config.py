TRANSFORM_CONFIG = {
    "Amazon Sale Report.csv": {
        "required_columns": ["Order ID", "Date", "Amount", "SKU"],
        "dedup_keys": ["Order ID", "Date", "SKU"],
        "column_types": {
            "Order ID": str,
            "Date": "datetime64[ns]",
            "Amount": float,
            "SKU": str
        }
    },
    "Cloud Warehouse Compersion Chart.csv": {
        "required_columns": ["Shiprocket", "INCREFF"],
        "dedup_keys": ["Shiprocket", "INCREFF"],
        "column_types": {
            "Shiprocket": float,
            "INCREFF": float
        }
    },
    "Expense IIGF.csv": {
        "required_columns": ["Recived Amount", "Expance"],
        "dedup_keys": ["Recived Amount", "Expance"],
        "column_types": {
            "Recived Amount": float,
            "Expance": str
        }
    },
    "International sale Report.csv": {
        "required_columns": ["DATE", "CUSTOMER", "PCS", "RATE"],
        "dedup_keys": ["DATE", "CUSTOMER", "SKU"],
        "column_types": {
            "DATE": "datetime64[ns]",
            "CUSTOMER": str,
            "PCS": int,
            "RATE": float,
            "GROSS AMT": float
        }
    },
    "May-2022.csv": {
        "required_columns": ["Sku", "Style Id", "Category", "TP", "Ajio MRP"],
        "dedup_keys": ["Sku", "Style Id", "Category"],
        "column_types": {
            "Sku": str,
            "Style Id": str,
            "Category": str,
            "TP": float,
            "Ajio MRP": float
        }
    },
    "P  L March 2021.csv": {
        "required_columns": ["Sku", "Style Id", "Category", "TP 1", "Ajio MRP"],
        "dedup_keys": ["Sku", "Style Id", "Category"],
        "column_types": {
            "Sku": str,
            "Style Id": str,
            "Category": str,
            "TP 1": float,
            "Ajio MRP": float
        }
    },
    "Sale Report.csv": {
        "required_columns": ["SKU Code", "Design No.", "Stock"],
        "dedup_keys": ["SKU Code", "Design No."],
        "column_types": {
            "SKU Code": str,
            "Design No.": str,
            "Stock": float
        }
    }
}
