# DE Zoomcamp Module 6: Streaming Solutions

## Setup

### Spark Structured Streaming
```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, window, count

spark = SparkSession.builder \
    .appName("taxi-streaming") \
    .getOrCreate()
```

---

## Question 1: Kafka Setup

**Answer**: Bootstrap servers configuration

```python
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "taxi-topic") \
    .load()
```

---

## Question 2: Stream Processing

**Answer**: Use `readStream` and `writeStream`

```python
# Read streaming data
df = spark.readStream.format("parquet").load("input-path/")

# Process
result = df.groupBy("PULocationID").count()

# Write output
result.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()
```

---

## Question 3: Window Operations

**Answer**: Use `window()` function

```python
df.groupBy(window("timestamp", "10 minutes")).count()
```

---

## Question 4: Watermarking

**Answer**: Handle late data with `withWatermark()`

```python
df.withWatermark("timestamp", "10 minutes") \
    .groupBy(window("timestamp", "5 minutes")).count()
```

---

## Question 5: Output Modes

**Answer**: complete, append, update

- **complete**: Output entire result table
- **append**: Output only new rows
- **update**: Output changed rows

---

## Question 6: Checkpoint Location

**Answer**: Fault tolerance with checkpointing

```python
result.writeStream \
    .outputMode("complete") \
    .format("console") \
    .option("checkpointLocation", "/checkpoint/path") \
    .start()
```

---

## Summary

| Question | Answer |
|----------|--------|
| Q1: Kafka | kafka.bootstrap.servers |
| Q2: Streaming | readStream/writeStream |
| Q3: Window | window() function |
| Q4: Watermark | withWatermark() |
| Q5: Modes | complete, append, update |
| Q6: Checkpoint | Fault tolerance |

---
**Status**: Complete ✅
**Repository**: https://github.com/dbillion/data-engineering-zoomcamp
**Branch**: homework-submissions-2026
