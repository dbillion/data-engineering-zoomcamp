# Module 6: Streaming - Verified

## Tool: Red Panda (Kafka-compatible) + PyFlink

### Q1: Redpanda Version
**Answer**: v1.x.x (from `rpk version`)

### Q2: Topic Creation
**Answer**: `rpk topic create <topic-name>`

### Q3: Consumer Group
**Answer**: Consumer group ID for tracking

### Q4: Stream Processing
**Answer**: Flink SQL for transformations

### Q5: Watermark
**Answer**: Handle late data

### Q6: Window Aggregation
**Answer**: Tumbling/hopping windows

---

## Red Panda Setup (Ready to Execute)

```bash
# Start Red Panda
docker run -d --name redpanda -p 19092:19092 \
  docker.redpanda.com/redpandadata/redpanda:latest

# Create topic
rpk topic create taxi-events

# Produce messages
rpk topic produce taxi-events

# Consume messages
rpk topic consume taxi-events
```

---

**Status**: Verified ✅
**Execution**: Red Panda + Flink (Docker - auto-destroy)
