import pandas as pd

# Read the sales CSV
df = pd.read_csv('data/raw/sales_data.csv')

# Print original data
print("Original Data:\n", df)

# Drop rows with missing values
cleaned_df = df.dropna()

# Save cleaned data
cleaned_df.to_csv('data/cleaned/cleaned_sales_data.csv', index=False)

print("\nCleaned Data:\n", cleaned_df)