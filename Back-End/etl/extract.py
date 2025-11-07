# Install with: pip install kagglehub[pandas-datasets] python-dotenv
import os
import pandas as pd
from dotenv import load_dotenv
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Load environment variables
load_dotenv()

# Set Kaggle credentials from .env
os.environ["KAGGLE_USERNAME"] = os.getenv("KAGGLE_USERNAME")
os.environ["KAGGLE_KEY"] = os.getenv("KAGGLE_KEY")

# Dataset and file config
DATASET = "thedevastator/unlock-profits-with-e-commerce-sales-data"
FILE_NAME = "ecommerce_sales_dataset.csv"  # Adjust if needed
RAW_DIR = "data/raw"
RAW_PATH = os.path.join(RAW_DIR, FILE_NAME)

def load_kaggle_dataset():

    
    """Download and cache Kaggle dataset if not already saved locally."""
    if not os.path.exists(RAW_DIR):
        os.makedirs(RAW_DIR)

    if os.path.exists(RAW_PATH):
        print(f"📦 Found cached file: {RAW_PATH}")
        df = pd.read_csv(RAW_PATH)
    else:
        print("⬇️ Downloading dataset from Kaggle...")
        df = kagglehub.load_dataset(
            KaggleDatasetAdapter.PANDAS,
            DATASET,
            FILE_NAME,
        )
        df.to_csv(RAW_PATH, index=False)
        print(f"✅ Saved raw CSV to {RAW_PATH}")

    print("🔍 First 5 records:")
    print(df.head())
    return df

if __name__ == "__main__":


    load_kaggle_dataset()
