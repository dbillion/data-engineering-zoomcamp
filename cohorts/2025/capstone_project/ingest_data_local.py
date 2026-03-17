"""
DE Zoomcamp Capstone: Data Ingestion (Local DuckDB Version)
Creates full ETL pipeline with DuckDB (no GCP credentials needed)
"""
import duckdb
import os

print("=== DE ZOOMCAMP CAPSTONE: LOCAL ETL PIPELINE ===\n")

# Create DuckDB database
con = duckdb.connect('capstone.db')
print("✅ Database created: capstone.db")

# Load data from URL
url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"
print(f"\nLoading data from: {url}")

# Create raw table
con.execute(f"""
CREATE OR REPLACE TABLE taxi_raw AS
SELECT * FROM read_parquet('{url}') LIMIT 10000
""")
raw_count = con.execute("SELECT COUNT(*) FROM taxi_raw").fetchone()[0]
print(f"✅ Raw table created: {raw_count:,} records")

# Create processed table (cleaned data)
con.execute("""
CREATE OR REPLACE TABLE taxi_processed AS
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
FROM taxi_raw
WHERE fare_amount > 0 AND trip_distance > 0
""")
processed_count = con.execute("SELECT COUNT(*) FROM taxi_processed").fetchone()[0]
print(f"✅ Processed table created: {processed_count:,} records")

# Create daily summary (aggregated)
con.execute("""
CREATE OR REPLACE TABLE taxi_daily_summary AS
SELECT 
    DATE(tpep_pickup_datetime) as trip_date,
    COUNT(*) as total_trips,
    AVG(fare_amount) as avg_fare,
    AVG(trip_distance) as avg_distance,
    SUM(total_amount) as total_revenue
FROM taxi_processed
GROUP BY DATE(tpep_pickup_datetime)
ORDER BY trip_date
""")
summary_count = con.execute("SELECT COUNT(*) FROM taxi_daily_summary").fetchone()[0]
print(f"✅ Daily summary created: {summary_count} days")

# Show sample results
print("\n=== SAMPLE RESULTS ===")
print("\nDaily Summary (first 7 days):")
results = con.execute("SELECT * FROM taxi_daily_summary LIMIT 7").fetchall()
for row in results:
    print(f"  {row[0]}: {row[1]:,} trips, ${row[2]:.2f} avg fare, ${row[4]:,.2f} revenue")

print("\n=== CAPSTONE ETL PIPELINE COMPLETE ✅ ===")
print("\nDatabase: capstone.db")
print("Tables:")
print("  - taxi_raw (raw data)")
print("  - taxi_processed (cleaned data)")
print("  - taxi_daily_summary (aggregated)")
print("\nTo query:")
print("  duckdb capstone.db")
print("  SELECT * FROM taxi_daily_summary;")

con.close()
