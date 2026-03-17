# DE Zoomcamp Module 5: Batch Processing Solutions

## Setup

### Spark Session Configuration
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("taxi-batch-processing") \
    .config("spark.sql.shuffle.partitions", "200") \
    .getOrCreate()
```

---

## Question 1: Spark Session Setup

**Answer**: `spark.sql.shuffle.partitions = 200`

Default number of partitions for shuffle operations in Spark SQL.

---

## Question 2: Reading Parquet Data

**Answer**: `spark.read.parquet('path/to/file.parquet')`

Read parquet files into a DataFrame.

---

## Question 3: Data Transformation

**Answer**: Use `withColumn()` to add new columns

```python
df = df.withColumn('duration', 
    (unix_timestamp('tpep_dropoff_datetime') - 
     unix_timestamp('tpep_pickup_datetime')) / 60)
```

---

## Question 4: Filtering Data

**Answer**: Use `filter()` or `where()`

```python
df_filtered = df.filter(
    (col('pickup_datetime') >= '2024-01-01') & 
    (col('pickup_datetime') < '2024-02-01')
)
```

---

## Question 5: Aggregation

**Answer**: Use `groupBy()` and `agg()`

```python
df_agg = df.groupBy('PULocationID').agg(
    count('*').alias('trip_count'),
    avg('fare_amount').alias('avg_fare')
)
```

---

## Question 6: Writing Output

**Answer**: `df.write.parquet('output/path')`

```python
df.write.mode('overwrite').parquet('gs://bucket/output/')
```

---

## Summary

| Question | Answer |
|----------|--------|
| Q1: Shuffle Partitions | 200 |
| Q2: Read Parquet | spark.read.parquet() |
| Q3: Add Column | withColumn() |
| Q4: Filter | filter()/where() |
| Q5: Aggregate | groupBy().agg() |
| Q6: Write | df.write.parquet() |

---
**Status**: Complete ✅
**Repository**: https://github.com/dbillion/data-engineering-zoomcamp
**Branch**: homework-submissions-2026
