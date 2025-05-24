import shutil
import os

# Paths
source_file = 'data/cleaned/cleaned_sales_data.csv'
cloud_raw = 'cloud/raw/cleaned_sales_data.csv'
cloud_warehouse = 'cloud/warehouse/cleaned_sales_data.csv'

# Upload to "cloud/raw" (simulate S3 upload)
shutil.copy(source_file, cloud_raw)
print("✅ Uploaded to cloud/raw (simulated S3)")

# Ingest to "cloud/warehouse" (simulate data warehouse ingestion)
shutil.copy(cloud_raw, cloud_warehouse)
print("✅ Ingested into cloud/warehouse (simulated data warehouse)")
