import os
import pandas as pd
import logging
from sqlalchemy import create_engine, text

LOG_DIR = 'logs/'
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, 'load.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

DB_URL = "postgresql://postgres:12345mmeli@db.inhbqpjnhuqfdybtzcsd.supabase.co:5432/postgres"

PROCESSED_DIR = "data/processed"
SCHEMA_PATH = "Back-End/sql/schema.sql"

def load_schema(engine):
    """
    Executes schema.sql to create tables if they don't exist.
    """
    with open(SCHEMA_PATH, "r") as f:
        schema_sql = f.read()
    with engine.connect() as conn:
        conn.execute(text(schema_sql))
        logging.info("✅ Executed schema.sql")

def load_csv_to_postgres(engine, filename, table_name):
    """
    Loads a cleaned CSV into PostgreSQL.
    """
    try:
        df = pd.read_csv(os.path.join(PROCESSED_DIR, filename))
        df.to_sql(table_name, engine, if_exists="append", index=False)
        logging.info(f"✅ Loaded {filename} into {table_name}")
        print(f"✅ Loaded {filename} into {table_name}")
    except Exception as e:
        logging.error(f"❌ Failed to load {filename}: {e}")
        print(f"❌ Failed to load {filename}: {e}")

if __name__ == "__main__":
    engine = create_engine(DB_URL)

    load_schema(engine)

    file_table_map = {
        "Amazon Sale Report.csv": "amazon_sale_report",
        "Cloud Warehouse Compersion Chart.csv": "cloud_warehouse_comparison",
        "Expense IIGF.csv": "expense_iigf",
        "International sale Report.csv": "international_sale_report",
        "May-2022.csv": "may_2022_pricing",
        "P  L March 2021.csv": "pl_march_2021",
        "Sale Report.csv": "sale_report"
    }

    for filename, table_name in file_table_map.items():
        load_csv_to_postgres(engine, filename, table_name)
