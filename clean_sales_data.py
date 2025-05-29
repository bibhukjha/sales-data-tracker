import pandas as pd

# Load the CSV file
df = pd.read_csv("retail_sales_data.csv")

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Handle missing values (if any)
df["category"] = df["category"].fillna("Unknown")
df["product"] = df["product"].fillna("Unknown")
df["customer_id"] = df["customer_id"].fillna("Unknown")

# Convert 'date' to datetime format
df["date"] = pd.to_datetime(df["date"], errors='coerce')

# Filter out rows with missing crucial fields (optional)
df = df.dropna(subset=["order_id", "price", "quantity", "date"])

# Calculate total amount per row (for analysis)
df["total_amount"] = df["price"] * df["quantity"]

# Save the cleaned data as a Parquet file
df.to_parquet("cleaned_sales_data.parquet", index=False)

print("✅ Cleaned and saved as Parquet successfully!")
