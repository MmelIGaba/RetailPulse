import os
import pandas as pd
import logging

# Setup logging
LOG_DIR = 'logs/'
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, 'transform.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def clean_dataframe(df: pd.DataFrame, required_columns: list, dedup_keys: list) -> pd.DataFrame:
    """
    Cleans a DataFrame by dropping rows with missing critical fields and deduplicating.
    """
    initial_rows = len(df)
    df_cleaned = df.dropna(subset=required_columns)
    df_cleaned = df_cleaned.drop_duplicates(subset=dedup_keys)
    final_rows = len(df_cleaned)

    logging.info(f"Cleaned DataFrame: {initial_rows - final_rows} rows removed")
    print(f"✅ Cleaned DataFrame: {initial_rows - final_rows} rows removed")

    return df_cleaned


def validate_types(df: pd.DataFrame, column_types: dict) -> pd.DataFrame:
    """
    Validates and converts column types based on expected schema.
    """
    for col, expected_type in column_types.items():
        try:
            df[col] = df[col].astype(expected_type)
            logging.info(f"Converted column '{col}' to {expected_type}")
        except Exception as e:
            logging.warning(f"Type conversion failed for column '{col}': {e}")
            print(f"⚠️ Type conversion failed for '{col}': {e}")
    return df


def transform_file(filepath: str, required_columns: list, dedup_keys: list, column_types: dict) -> pd.DataFrame:
    """
    Full transform pipeline for a single CSV file.
    """
    try:
        df = pd.read_csv(filepath)
        logging.info(f"Loaded file: {filepath}")
        df = clean_dataframe(df, required_columns, dedup_keys)
        df = validate_types(df, column_types)
        return df
    except Exception as e:
        logging.error(f"Error transforming file {filepath}: {e}")
        print(f"❌ Error transforming file {filepath}: {e}")
        return pd.DataFrame()


if __name__ == "__main__":
    # Example usage
    FILEPATH = 'data/raw/Sale Report.csv'
    REQUIRED = ['ProductID', 'SaleAmount']
    DEDUP_KEYS = ['ProductID', 'Date', 'StoreID']
    COLUMN_TYPES = {
        'ProductID': str,
        'SaleAmount': float,
        'Date': 'datetime64[ns]',
        'StoreID': str
    }

    df_transformed = transform_file(FILEPATH, REQUIRED, DEDUP_KEYS, COLUMN_TYPES)
    print(df_transformed.head())
