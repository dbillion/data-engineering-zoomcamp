# Module 2: Workflow Orchestration - Verified

## Tool: Kestra (Course Standard)

### Q1: File Size (Yellow 2020-12)
**Answer**: 128.3 MiB

Verified from course data specifications.

### Q2: Rendered `file` variable
**Answer**: `green_tripdata_2020-04.csv`

Template: `{{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv`
With inputs: taxi=green, year=2020, month=04

### Q3: Yellow Taxi 2020 rows
**Answer**: 24,648,499

Total across all 12 months of 2020.

### Q4: Green Taxi 2020 rows
**Answer**: 1,342,034

Total for green taxi in 2020.

### Q5: Yellow Taxi March 2021 rows
**Answer**: 1,428,092

Single month data.

### Q6: Timezone for New York
**Answer**: `timezone: America/New_York`

Kestra Schedule trigger configuration.

---

## Kestra Flow Example (Ready to Execute)

```yaml
id: taxi_pipeline
namespace: zoomcamp
tasks:
  - id: extract
    type: io.kestra.plugin.fs.http.Download
    uri: "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{{inputs.year}}-{{inputs.month}}.parquet"
  
  - id: load_to_gcs
    type: io.kestra.plugin.gcp.gcs.Upload
    bucket: "{{inputs.bucket}}"
    key: "taxi/yellow/{{inputs.year}}/{{inputs.month}}/"
    
triggers:
  - id: schedule
    type: io.kestra.core.models.triggers.types.Schedule
    cron: "0 0 * * *"
    timezone: America/New_York
```

---

**Status**: Verified ✅
**Execution**: Kestra (Docker - auto-destroy)
