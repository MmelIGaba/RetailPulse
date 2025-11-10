import os
import logging
import pandas as pd
from sqlalchemy import create_engine
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# ------------------------------------------------
# 1. LOAD ENVIRONMENT VARIABLES
# ------------------------------------------------
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")
TABLE_NAME = os.getenv("TABLE_NAME")

AZURE_STORAGE_ACCOUNT = os.getenv("AZURE_STORAGE_ACCOUNT")
AZURE_STORAGE_KEY = os.getenv("AZURE_STORAGE_KEY")
CONTAINER_NAME = os.getenv("CONTAINER_NAME")
BLOB_NAME = os.getenv("BLOB_NAME")

LOCAL_FILE_PATH = os.getenv("LOCAL_FILE_PATH", "data/processed/your_file.csv")

# ------------------------------------------------
# 2. SETUP LOGGING
# ------------------------------------------------
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(LOG_DIR, "load.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ------------------------------------------------
# 3. MAIN LOAD FUNCTION
# ------------------------------------------------
def load_to_azure():
    """Load cleaned CSV data into Azure PostgreSQL and upload to Azure Blob."""
    # -----------------------
    # Database Connection
    # -----------------------
    try:
        logging.info("Connecting to Azure PostgreSQL...")
        engine = create_engine(
            f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=require"
        )
        logging.info("✅ PostgreSQL connection established.")
    except Exception as e:
        logging.error(f"❌ Failed to connect to Azure PostgreSQL: {e}")
        print(f"❌ Failed to connect to Azure PostgreSQL: {e}")
        return

    # -----------------------
    # Load CSV into PostgreSQL
    # -----------------------
    try:
        df = pd.read_csv(LOCAL_FILE_PATH)
        df.to_sql(TABLE_NAME, engine, if_exists="replace", index=False)

        db_count = pd.read_sql(f"SELECT COUNT(*) FROM {TABLE_NAME}", engine).iloc[0, 0]
        logging.info(f"✅ Loaded {len(df)} rows into {TABLE_NAME}. DB count: {db_count}")

        print(f"✅ Data successfully loaded into Azure PostgreSQL table: {TABLE_NAME}")
    except Exception as e:
        logging.error(f"❌ Failed to load CSV into DB: {e}")
        print(f"❌ Failed to load CSV into DB: {e}")
        return

    # -----------------------
    # Upload to Azure Blob Storage
    # -----------------------
    try:
        connection_string = (
            f"DefaultEndpointsProtocol=https;"
            f"AccountName={AZURE_STORAGE_ACCOUNT};"
            f"AccountKey={AZURE_STORAGE_KEY};"
            f"EndpointSuffix=core.windows.net"
        )

        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        blob_client = blob_service_client.get_blob_client(
            container=CONTAINER_NAME,
            blob=BLOB_NAME
        )

        with open(LOCAL_FILE_PATH, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

        logging.info(f"✅ Uploaded file to Azure Blob: {CONTAINER_NAME}/{BLOB_NAME}")
        print(f"✅ File successfully uploaded to Azure Blob: {CONTAINER_NAME}/{BLOB_NAME}")

    except Exception as e:
        logging.error(f"❌ Azure Blob upload failed: {e}")
        print(f"❌ Azure Blob upload failed: {e}")
        return


# ------------------------------------------------
# 4. RUN SCRIPT DIRECTLY
# ------------------------------------------------
if __name__ == "__main__":
    print("🚀 Starting LOAD process...")
    load_to_azure()
    print("✅ Load process completed. Check logs/load.log for details.")
