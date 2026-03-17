# DE Zoomcamp - Execution Plan

## Resource Management Policy

### ✅ KEEP (Local Resources)
- Docker containers (Kestra, Red Panda, Flink, Metabase)
- PySpark installation
- dbt installation
- Local verification files
- Code templates

### 🗑️ DESTROY (Cloud Resources Only)
After each module execution:
- BigQuery datasets created
- GCS buckets created (if any)
- Temporary GCP resources

---

## Execution Commands

### Module 2: Kestra
```bash
# Start (already done)
docker run -d -p 8080:8080 kestra/kestra:latest server local

# Access: http://localhost:8080
# KEEP container for review
```

### Module 3: BigQuery (DuckDB Verified)
```bash
# Cleanup GCP only
gcloud bigquery datasets delete taxi_rides --recursive --force
```

### Module 4: dbt + BigQuery
```bash
# Run dbt models
dbt run

# Cleanup GCP only
gcloud bigquery datasets delete dbt_zoomcamp --recursive --force
```

### Module 5: PySpark
```bash
# Run locally (no cleanup needed)
python batch_processing.py
```

### Module 6: Streaming
```bash
# Start services (already done)
docker run -d --name redpanda -p 19092:19092 redpandadata/redpanda

# KEEP containers for review
```

### Project: Dashboard
```bash
# Start Metabase (already done)
docker run -d -p 3001:3000 metabase/metabase

# KEEP container for review
```

---

## GCP Cleanup Script

```bash
#!/bin/bash
# cleanup_gcp.sh

echo "Cleaning up GCP resources..."

# Delete BigQuery datasets
gcloud bigquery datasets delete taxi_rides --recursive --force --quiet
gcloud bigquery datasets delete dbt_zoomcamp --recursive --force --quiet

# Delete GCS buckets
gsutil rm -r gs://zoomcamp-* 2>/dev/null || true

echo "GCP cleanup complete!"
```

---

**Status**: Ready to Execute
**Auto-Destroy**: Cloud resources only ✅
**Local Resources**: Retained for review ✅
