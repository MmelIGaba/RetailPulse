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
import os
import pandas as pd
import importlib

etl_module = importlib.import_module("Back-End.etl.transform")
config_module = importlib.import_module("Back-End.etl.transform_config")

transform_file = getattr(etl_module, "transform_file")
TRANSFORM_CONFIG = getattr(config_module, "TRANSFORM_CONFIG")

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
os.makedirs(PROCESSED_DIR, exist_ok=True)

for filename in os.listdir(RAW_DIR):
    if filename.endswith(".csv") and filename in TRANSFORM_CONFIG:
        print(f"\n🔄 Transforming: {filename}")
        config = TRANSFORM_CONFIG[filename]
        try:
            df_transformed = transform_file(
                filepath=os.path.join(RAW_DIR, filename),
                required_columns=config["required_columns"],
                dedup_keys=config["dedup_keys"],
                column_types=config["column_types"]
            )
            output_path = os.path.join(PROCESSED_DIR, filename)
            df_transformed.to_csv(output_path, index=False)
            print(f"✅ Saved cleaned file to: {output_path}")
        except Exception as e:
            print(f"❌ {filename}: Transform failed — {e}")
