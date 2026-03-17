# DE Zoomcamp Capstone Project: NYC Taxi Analytics Pipeline

## Architecture

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐     ┌──────────────┐
│  Data Source│────▶│  Ingestion   │────▶│  BigQuery   │────▶│  Metabase    │
│  (NYC TLC)  │     │  (Python)    │     │  (Warehouse)│     │  (Dashboard) │
└─────────────┘     └──────────────┘     └─────────────┘     └──────────────┘
```

## Project Components

### 1. Data Ingestion
- Downloads NYC Yellow Taxi data from GitHub
- Loads to BigQuery via Python

### 2. Data Warehouse (BigQuery)
- Raw table: `taxi_raw`
- Processed table: `taxi_processed`
- Aggregated table: `taxi_daily_summary`

### 3. Analytics Engineering (dbt)
- Staging models
- Core fact/dim tables
- Data quality tests

### 4. Dashboard (Metabase)
- Daily trip counts
- Revenue trends
- Popular pickup zones
- Average trip distance

## Execution

```bash
# 1. Run ingestion
python3 ingest_data.py

# 2. Run dbt models
dbt run

# 3. Start Metabase
docker run -d -p 3001:3000 metabase/metabase

# 4. Cleanup (after review)
bq rm -f -r zoomcamp_capstone
```

## Status: ✅ COMPLETE
