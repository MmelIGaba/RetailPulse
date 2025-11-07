import os
import pandas as pd
import importlib

etl_module = importlib.import_module("Back-End.etl.transform")
config_module = importlib.import_module("Back-End.etl.transform_config")

clean_dataframe = getattr(etl_module, "clean_dataframe")
TRANSFORM_CONFIG = getattr(config_module, "TRANSFORM_CONFIG")

RAW_DIR = "data/raw"

for filename in os.listdir(RAW_DIR):
    if filename.endswith(".csv") and filename in TRANSFORM_CONFIG:
        print(f"\n🔍 Testing: {filename}")
        config = TRANSFORM_CONFIG[filename]
        try:
            df = pd.read_csv(os.path.join(RAW_DIR, filename))
            df_cleaned = clean_dataframe(df, config["required_columns"], config["dedup_keys"])
            print(f"✅ {filename}: {len(df_cleaned)} rows after cleaning")
        except Exception as e:
            print(f"❌ {filename}: Error during cleaning — {e}")
