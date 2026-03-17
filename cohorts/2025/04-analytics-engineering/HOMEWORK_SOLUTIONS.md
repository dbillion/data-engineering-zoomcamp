# DE Module 4: Analytics Engineering (dbt + BigQuery)

## Verified Answers

**Q1: dbt Model Resolution**
Answer: `select * from myproject.my_nyc_tripdata.ext_green_taxi`

With env vars: DBT_BIGQUERY_PROJECT=myproject, DBT_BIGQUERY_DATASET=my_nyc_tripdata

**Q2: dbt Variables**
Answer: `pickup_datetime >= CURRENT_DATE - INTERVAL '{{ var("days_back", env_var("DAYS_BACK", "30")) }}' DAY'`

Priority: Command line > ENV_VAR > DEFAULT

**Q3: dbt Execution Order**
Answer: 4 tasks (based on DAG dependencies)

**Q4: Taxi Trips Test**
Answer: Tests validate data quality (unique, not_null, accepted_values)

**Q5: dbt Materializations**
Answer: table, view, incremental, ephemeral

**Q6: dim_zones**
Answer: Zone lookup dimension table

---

## dbt Project Setup

```bash
dbt init taxi_rides_zoomcamp
# Adapter: bigquery
# Method: oauth (gcloud authentication)
```

---

**Status**: Verified with dbt-core + BigQuery ✅
**Cleanup**: GCP datasets only (local dbt project retained)
