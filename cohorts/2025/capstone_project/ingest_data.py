"""
DE Zoomcamp Capstone: Data Ingestion Script
Downloads NYC Yellow Taxi data and loads to BigQuery
"""
import pandas as pd
from google.cloud import bigquery
import os

print("=== DE ZOOMCAMP CAPSTONE: DATA INGESTION ===\n")

# Initialize BigQuery client
os.environ['GOOGLE_CLOUD_PROJECT'] = 'future-abode-338616'
client = bigquery.Client()

# Create dataset
dataset_id = "future-abode-338616.zoomcamp_capstone"
dataset = bigquery.Dataset(dataset_id)
try:
    client.create_dataset(dataset, exists_ok=True)
    print(f"✅ Dataset created: {dataset_id}")
except Exception as e:
    print(f"⚠️ Dataset issue: {e}")

# Load sample data (January 2024)
url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"
print(f"\nLoading data from: {url}")

# Read with DuckDB (faster for this demo)
import duckdb
con = duckdb.connect()
df = con.execute(f"SELECT * FROM read_parquet('{url}') LIMIT 10000").df()
print(f"✅ Loaded {len(df):,} records")

# Load to BigQuery
table_id = f"{dataset_id}.taxi_raw"
job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")
job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
job.result()
print(f"✅ Loaded to BigQuery: {table_id}")

# Create processed table
processed_sql = f"""
CREATE OR REPLACE TABLE `{dataset_id}.taxi_processed` AS
SELECT 
    VendorID,
    tpep_pickup_datetime,
    tpep_dropoff_datetime,
    passenger_count,
    trip_distance,
    fare_amount,
    tip_amount,
    total_amount,
    PULocationID,
    DOLocationID
FROM `{dataset_id}.taxi_raw`
WHERE fare_amount > 0 AND trip_distance > 0
"""
client.query(processed_sql).result()
print(f"✅ Created processed table")

# Create daily summary
summary_sql = f"""
CREATE OR REPLACE TABLE `{dataset_id}.taxi_daily_summary` AS
SELECT 
    DATE(tpep_pickup_datetime) as trip_date,
    COUNT(*) as total_trips,
    AVG(fare_amount) as avg_fare,
    AVG(trip_distance) as avg_distance,
    SUM(total_amount) as total_revenue
FROM `{dataset_id}.taxi_processed`
GROUP BY DATE(tpep_pickup_datetime)
ORDER BY trip_date
"""
client.query(summary_sql).result()
print(f"✅ Created daily summary table")

print("\n✅ CAPSTONE DATA INGESTION COMPLETE")
print(f"Dataset: {dataset_id}")
print("Tables created:")
print("  - taxi_raw (raw data)")
print("  - taxi_processed (cleaned data)")
print("  - taxi_daily_summary (aggregated)")
