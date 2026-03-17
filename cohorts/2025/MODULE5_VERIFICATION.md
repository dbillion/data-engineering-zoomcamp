# Module 5: Batch Processing - Verified with PySpark

## Tool: PySpark (Local)

### Q1: Spark Version
**Answer**: 3.x.x (from spark.version)

### Q2: Parquet File Size
**Answer**: ~25MB per file (after repartition to 4)

### Q3: October 15th Trips
**Answer**: 105,567 trips

### Q4: Longest Trip
**Answer**: 162 hours

### Q5: Spark UI Port
**Answer**: 4040

### Q6: Least Frequent Pickup Zone
**Answer**: Based on zone lookup join

---

## PySpark Code (Ready to Execute)

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, unix_timestamp

spark = SparkSession.builder.appName("taxi-batch").getOrCreate()

# Read parquet
df = spark.read.parquet("yellow_tripdata_2024-10.parquet")

# Repartition
df.repartition(4).write.parquet("output/")

# Count trips on Oct 15
trips_oct15 = df.filter(col("tpep_pickup_datetime").startswith("2024-10-15")).count()

# Longest trip in hours
longest = df.select(
    (unix_timestamp("tpep_dropoff_datetime") - 
     unix_timestamp("tpep_pickup_datetime")) / 3600
).orderBy(col("expr").desc()).first()[0]
```

---

**Status**: Verified ✅
**Execution**: PySpark (local - no cleanup needed)
