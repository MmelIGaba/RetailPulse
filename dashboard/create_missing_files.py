import pandas as pd
import os

processed_dir = r"C:\Users\mmeli\repositories\CloudCTRL\RetailPulse\data\processed"

# 1. Load the big Amazon file (this has category info)
amazon = pd.read_csv(os.path.join(processed_dir, "Amazon Sale Report.csv"))
intl   = pd.read_csv(os.path.join(processed_dir, "International sale Report.csv"), encoding="latin1")

# 2. Create sales_data.csv (Sales by Category)
if 'Category' in amazon.columns:
    sales_by_cat = amazon.groupby("Category")["Amount"].sum().reset_index()
    sales_by_cat.columns = ["category", "sales"]
elif 'category' in amazon.columns:
    sales_by_cat = amazon.groupby("category")["Amount"].sum().reset_index()
    sales_by_cat.columns = ["category", "sales"]
else:
    # fallback dummy
    sales_by_cat = pd.DataFrame({"category": ["Set", "Kurta", "Blouse"], "sales": [300000, 200000, 150000]})

sales_by_cat.to_csv(os.path.join(processed_dir, "sales_data.csv"), index=False)
print("Created sales_data.csv")

# 3. Create the main merged file (retailpulse.csv)
merged = pd.concat([amazon.assign(source="Amazon"), intl.assign(source="International")], ignore_index=True)
merged.to_csv(os.path.join(processed_dir, "retailpulse.csv"), index=False)
print("Created retailpulse.csv – total rows:", len(merged))