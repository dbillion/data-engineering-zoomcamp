# DE Zoomcamp Module 3: Data Warehouse Solutions

## Prerequisites
- GCP Project with BigQuery API enabled
- Service Account with BigQuery and GCS permissions
- Yellow Taxi Trip Records for January 2024 - June 2024 uploaded to GCS

## Setup

### Create External Table
```sql
CREATE OR REPLACE EXTERNAL TABLE `project.dataset.yellow_tripdata_external`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://bucket/path/yellow_tripdata_2024-*.parquet']
);
```

### Create Regular Table
```sql
CREATE OR REPLACE TABLE `project.dataset.yellow_tripdata` AS
SELECT * FROM `project.dataset.yellow_tripdata_external`;
```

---

## Question 1: Count of Records for 2024 Yellow Taxi Data

**Answer**: 20,332,093

```sql
SELECT COUNT(*) FROM `project.dataset.yellow_tripdata`
WHERE tpep_pickup_datetime >= '2024-01-01' 
  AND tpep_pickup_datetime < '2024-07-01';
```

---

## Question 2: Distinct PULocationIDs - Estimated Bytes Read

**Answer**: 0 MB for the External Table and 155.12 MB for the Materialized Table

```sql
-- External Table
SELECT COUNT(DISTINCT PULocationID) FROM `project.dataset.yellow_tripdata_external`;
-- Estimated bytes: 0 MB (metadata only for COUNT DISTINCT)

-- Regular Table  
SELECT COUNT(DISTINCT PULocationID) FROM `project.dataset.yellow_tripdata`;
-- Estimated bytes: 155.12 MB (full table scan)
```

---

## Question 3: Column Store Behavior

**Answer**: BigQuery is a columnar database, and it only scans the specific columns requested in the query. 
Querying two columns (PULocationID, DOLocationID) requires reading more data than querying one column 
(PULocationID), leading to a higher estimated number of bytes processed.

---

## Question 4: Records with fare_amount of 0

**Answer**: 128,210

```sql
SELECT COUNT(*) FROM `project.dataset.yellow_tripdata`
WHERE fare_amount = 0;
```

---

## Question 5: Best Optimization Strategy

**Answer**: Partition by tpep_dropoff_datetime and Cluster on VendorID

```sql
CREATE OR REPLACE TABLE `project.dataset.yellow_tripdata_optimized`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID AS
SELECT * FROM `project.dataset.yellow_tripdata`;
```

---

## Question 6: Distinct VendorIDs (March 1-15, 2024)

**Answer**: 4 (VendorIDs: 1, 2, 3, 4)

```sql
SELECT DISTINCT VendorID FROM `project.dataset.yellow_tripdata`
WHERE tpep_dropoff_datetime >= '2024-03-01' 
  AND tpep_dropoff_datetime <= '2024-03-15'
ORDER BY VendorID;
```

---

## Summary

| Question | Answer |
|----------|--------|
| Q1: Record Count | 20,332,093 |
| Q2: Bytes Read | 0 MB External, 155.12 MB Table |
| Q3: Columnar DB | Column-scanning behavior |
| Q4: Zero Fare | 128,210 |
| Q5: Optimization | Partition by dropoff, Cluster by Vendor |
| Q6: VendorIDs | 4 distinct |

---
**Status**: Complete ✅
**Repository**: https://github.com/dbillion/data-engineering-zoomcamp
**Branch**: homework-submissions-2026
