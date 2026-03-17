-- DE Zoomcamp Capstone: dbt-style SQL models

-- Staging model: stg_taxi_trips
-- Cleans and standardizes raw taxi data
CREATE OR REPLACE VIEW stg_taxi_trips AS
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
    DOLocationID,
    EXTRACT(HOUR FROM tpep_pickup_datetime) as pickup_hour,
    EXTRACT(DAYOFWEEK FROM tpep_pickup_datetime) as day_of_week
FROM taxi_processed
WHERE fare_amount > 0
  AND trip_distance > 0
  AND passenger_count > 0;

-- Core model: fact_trips
-- Main fact table for analytics
CREATE OR REPLACE VIEW fact_trips AS
SELECT 
    MD5(CONCAT(VendorID, '-', tpep_pickup_datetime)) as trip_id,
    tpep_pickup_datetime,
    tpep_dropoff_datetime,
    TIMESTAMP_DIFF(tpep_dropoff_datetime, tpep_pickup_datetime, MINUTE) as trip_duration_min,
    trip_distance,
    fare_amount,
    tip_amount,
    total_amount,
    PULocationID as pickup_zone_id,
    DOLocationID as dropoff_zone_id
FROM stg_taxi_trips;

-- Core model: dim_zones
-- Dimension table for zones
CREATE OR REPLACE VIEW dim_zones AS
SELECT DISTINCT 
    PULocationID as zone_id,
    'pickup' as zone_type
FROM taxi_processed
UNION
SELECT DISTINCT 
    DOLocationID as zone_id,
    'dropoff' as zone_type
FROM taxi_processed;

-- Aggregation: daily_revenue
-- Daily revenue summary
CREATE OR REPLACE VIEW daily_revenue AS
SELECT 
    DATE(tpep_pickup_datetime) as trip_date,
    COUNT(*) as total_trips,
    SUM(fare_amount) as total_fare,
    SUM(tip_amount) as total_tips,
    SUM(total_amount) as total_revenue,
    AVG(trip_distance) as avg_distance
FROM fact_trips
GROUP BY DATE(tpep_pickup_datetime)
ORDER BY trip_date;

-- Data Quality Tests
-- Test 1: No negative fares
SELECT COUNT(*) as negative_fares FROM fact_trips WHERE fare_amount < 0;
-- Expected: 0

-- Test 2: No null timestamps
SELECT COUNT(*) as null_timestamps FROM fact_trips WHERE tpep_pickup_datetime IS NULL;
-- Expected: 0

-- Test 3: Reasonable trip duration (0-24 hours)
SELECT COUNT(*) as unreasonable_duration FROM fact_trips WHERE trip_duration_min < 0 OR trip_duration_min > 1440;
-- Expected: 0
