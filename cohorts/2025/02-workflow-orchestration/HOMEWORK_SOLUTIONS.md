# DE Zoomcamp Module 2: Workflow Orchestration Solutions

## Quiz Answers

### Q1: Uncompressed file size (Yellow 2020-12)
**Answer**: 128.3 MiB

The extracted CSV file size for yellow taxi December 2020.

### Q2: Rendered value of `file` variable
**Answer**: `green_tripdata_2020-04.csv`

When taxi=green, year=2020, month=04:
```
{{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv
= green_tripdata_2020-04.csv
```

### Q3: Yellow Taxi 2020 rows
**Answer**: 24,648,499

Total rows across all 12 months of 2020.

### Q4: Green Taxi 2020 rows
**Answer**: 1,342,034

Total rows for green taxi in 2020.

### Q5: Yellow Taxi March 2021 rows
**Answer**: 1,428,092

Single month data for March 2021.

### Q6: Timezone configuration for New York
**Answer**: Add a `timezone` property set to `America/New_York` in the `Schedule` trigger configuration

Correct Kestra syntax:
```yaml
triggers:
  - id: schedule
    type: io.kestra.core.models.triggers.types.Schedule
    cron: "0 0 * * *"
    timezone: America/New_York
```

---
**Status**: Complete ✅
**Repository**: https://github.com/dbillion/data-engineering-zoomcamp
**Branch**: homework-submissions-2026
