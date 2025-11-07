import os
import logging

# Use os.path.join instead of hardcoded slashes
RAW_DIR = os.path.join("data", "raw")
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "extract.log")

# Ensure the log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def ensure_raw_csv_exists():
    kaggle_url = "https://www.kaggle.com/datasets/thedevastator/unlock-profits-with-e-commerce-sales-data"

    try:
        # Ensure raw data directory exists
        os.makedirs(RAW_DIR, exist_ok=True)

        # Find all CSV files (case-insensitive)
        csv_files = [f for f in os.listdir(RAW_DIR) if f.lower().endswith(".csv")]

        if not csv_files:
            logging.warning("No CSV file found in data/raw/")
            print("⚠️ No CSV file found in 'data/raw/'.")
            print(
                f"Please download the dataset from {kaggle_url} and place it in the '{RAW_DIR}' folder."
            )
            return False

        logging.info(f"CSV file(s) found: {csv_files}")
        return {"status": True, "files": csv_files}

    except Exception as e:
        logging.error(f"Error during CSV check: {e}")
        return False


if __name__ == "__main__":
    ensure_raw_csv_exists()
