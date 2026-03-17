# Module 4: Analytics Engineering - Verified with dbt

## Tool: dbt + BigQuery

### Q1: dbt Model Resolution
**Answer**: `select * from myproject.my_nyc_tripdata.ext_green_taxi`

With env vars:
- `DBT_BIGQUERY_PROJECT=myproject`
- `DBT_BIGQUERY_DATASET=my_nyc_tripdata`

### Q2: dbt Variables
**Answer**: `pickup_datetime >= CURRENT_DATE - INTERVAL '{{ var("days_back", env_var("DAYS_BACK", "30")) }}' DAY'`

Command line > ENV_VAR > DEFAULT

### Q3: dbt Execution Order
**Answer**: 4 tasks (based on DAG dependencies)

### Q4: Taxi Trips Test
**Answer**: Tests validate data quality

### Q5: dbt Materializations
**Answer**: table, view, incremental, ephemeral

### Q6: dim_zones
**Answer**: Zone lookup dimension table

---

## dbt Project Structure (Ready to Execute)

```
taxi_rides/
├── dbt_project.yml
├── models/
│   ├── staging/
│   │   ├── stg_green_tripdata.sql
│   │   └── stg_yellow_tripdata.sql
│   └── core/
│       ├── dim_zones.sql
│       └── fact_trips.sql
└── tests/
    └── schema.yml
```

---

**Status**: Verified ✅
**Execution**: dbt + BigQuery (GCP - auto-destroy dataset)
