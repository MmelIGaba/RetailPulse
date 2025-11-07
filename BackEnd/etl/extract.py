import os
import logging

RAW_DIR = 'data/raw/'
LOG_DIR = 'logs/'
LOG_FILE = os.path.join(LOG_DIR, 'extract.log')

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def ensure_raw_csv_exists():
    try:
        os.makedirs(RAW_DIR, exist_ok=True)

        csv_files = [f for f in os.listdir(RAW_DIR) if f.endswith('.csv')]

        if not csv_files:
            logging.warning("No CSV file found in data/raw/")
            kggleURL = "https://www.kaggle.com/datasets/thedevastator/unlock-profits-with-e-commerce-sales-data"
            print("⚠️ No CSV file found in 'data/raw/'.")
            print(f"Please download the dataset from {kggleURL} and place it in the 'data/raw/' folder.")
            return False

        logging.info(f"CSV file(s) found: {csv_files}")
        print(f"✅ Found CSV file(s): {csv_files}")
        return True

    except Exception as e:
        logging.error(f"Error during CSV check: {e}")
        print(f"❌ Error checking CSV files: {e}")
        return False

if __name__ == "__main__":
    ensure_raw_csv_exists()
