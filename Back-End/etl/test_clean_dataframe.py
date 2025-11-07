import pandas as pd
from etl.transform import clean_dataframe  # Adjust import if needed

# Sample data with nulls and duplicates
data = {
    'ProductID': ['A1', 'A2', None, 'A1', 'A3'],
    'SaleAmount': [100, None, 200, 100, 300],
    'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-01', '2022-01-04'],
    'StoreID': ['S1', 'S2', 'S3', 'S1', 'S4']
}

df = pd.DataFrame(data)

# Define cleaning rules
required_columns = ['ProductID', 'SaleAmount']
dedup_keys = ['ProductID', 'Date', 'StoreID']

# Apply cleaning
df_cleaned = clean_dataframe(df, required_columns, dedup_keys)

# Show results
print("Original DataFrame:")
print(df)
print("\nCleaned DataFrame:")
print(df_cleaned)
