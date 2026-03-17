# DE Zoomcamp Module 4: Analytics Engineering Solutions

## Setup

### dbt Project Structure
```
taxi_rides/
├── dbt_project.yml
├── models/
│   ├── staging/
│   │   ├── stg_green_tripdata.sql
│   │   └── stg_yellow_tripdata.sql
│   └── core/
│       ├── dim_zones.sql
│       ├── fact_trips.sql
│       └── dm_monthly_zone_revenue.sql
├── seeds/
│   └── taxi_zone_lookup.csv
└── tests/
    └── schema.yml
```

---

## Question 1: Understanding dbt Models

**Answer**: A dbt model is a SELECT statement that defines a transformation

dbt models are SQL files containing SELECT statements that define how to transform source data into analytics-ready tables.

---

## Question 2: dbt Materializations

**Answer**: table, view, incremental, ephemeral

These are the four main dbt materialization strategies:
- **table**: Creates a physical table
- **view**: Creates a view
- **incremental**: Only processes new data
- **ephemeral**: Temporary CTE, not materialized

---

## Question 3: Staging Models

**Answer**: Rename columns, cast data types, filter records

Staging models perform basic transformations:
- Rename columns to consistent naming
- Cast data types appropriately
- Filter out nulls/invalid records
- Add basic business logic

---

## Question 4: Core Models (fact_trips)

**Answer**: Join green and yellow taxi data with zone lookup

```sql
{{ config(materialized='table') }}

WITH green_data AS (
    SELECT * FROM {{ ref('stg_green_tripdata') }}
),
yellow_data AS (
    SELECT * FROM {{ ref('stg_yellow_tripdata') }}
),
combined AS (
    SELECT * FROM green_data
    UNION ALL
    SELECT * FROM yellow_data
)
SELECT 
    t.*,
    z.zone as pickup_zone,
    z.borough as pickup_borough
FROM combined t
JOIN {{ ref('dim_zones') }} z ON t.PULocationID = z.locationid
```

---

## Question 5: dbt Tests

**Answer**: unique, not_null, accepted_values, relationships

Standard dbt schema tests:
- **unique**: Ensures no duplicates
- **not_null**: Ensures no null values
- **accepted_values**: Validates against a list
- **relationships**: Validates foreign key relationships

---

## Question 6: Dimension Table (dim_zones)

**Answer**: Contains unique zone information

```sql
{{ config(materialized='table') }}

SELECT 
    locationid,
    borough,
    zone,
    service_zone
FROM {{ source('staging', 'taxi_zone_lookup') }}
WHERE locationid != 264  -- Exclude 'NV' (No Vehicle)
```

---

## Summary

| Question | Answer |
|----------|--------|
| Q1: dbt Model | SELECT statement transformation |
| Q2: Materializations | table, view, incremental, ephemeral |
| Q3: Staging | Rename, cast, filter |
| Q4: fact_trips | Union green + yellow with zones |
| Q5: Tests | unique, not_null, accepted_values, relationships |
| Q6: dim_zones | Zone lookup table |

---
**Status**: Complete ✅
**Repository**: https://github.com/dbillion/data-engineering-zoomcamp
**Branch**: homework-submissions-2026
