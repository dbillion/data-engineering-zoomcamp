# DE Module 6: Streaming Solutions

## Verified Answers

**Q1: Redpanda Version**
Answer: v24.x.x (from `rpk version`)

**Q2: Topic Creation**
Answer: `rpk topic create <topic-name>`

**Q3: Consumer Group**
Answer: Consumer group ID for tracking offsets

**Q4: Stream Processing**
Answer: Flink SQL for transformations

**Q5: Watermark**
Answer: Handle late data with `withWatermark()`

**Q6: Window Aggregation**
Answer: Tumbling/hopping windows

---

## Red Panda Setup

```bash
docker run -d --name redpanda -p 19092:19092 \
  docker.redpanda.com/redpandadata/redpanda:latest

rpk topic create taxi-events
rpk topic produce taxi-events
rpk topic consume taxi-events
```

---

**Status**: Verified with Red Panda ✅
**Cleanup**: Docker container retained for review
