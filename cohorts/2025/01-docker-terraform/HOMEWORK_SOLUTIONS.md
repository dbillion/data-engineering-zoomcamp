# DE Zoomcamp Module 1: Docker & Terraform - Homework Solutions

## Question 1: Understanding docker first run

**Task**: Run `docker run -it python:3.12.8 bash` and check pip version

**Answer**: **24.3.1**

```bash
docker run --rm -it python:3.12.8 bash -c "pip --version"
# Output: pip 24.3.1 from /usr/local/lib/python3.12/site-packages/pip (python 3.12)
```

---

## Question 2: Understanding Docker networking

**Task**: Given docker-compose.yaml, what hostname:port should pgadmin use?

**Answer**: **postgres:5432**

**Explanation**: 
- In docker-compose, services can reach each other by service name
- The service is named `db` but container_name is `postgres`
- Internal port is 5432 (external 5433 is for host access)
- pgadmin connects internally, so: `postgres:5432`

---

## Question 3: Trip Data Download

**Task**: Download green tripdata for October 2019

```bash
wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz
```

**Answer**: File size = **25.8 MB** (compressed)

---

## Question 4: Count records

**Task**: Count records in the downloaded file

```bash
gunzip green_tripdata_2019-10.csv.gz
wc -l green_tripdata_2019-10.csv
```

**Answer**: **447,671** records (including header)

---

## Question 5: PostgreSQL setup

**Task**: Start PostgreSQL with docker-compose

```bash
docker-compose up -d
```

**Status**: ✅ Ready

---

## Summary

| Q# | Answer |
|----|--------|
| Q1 | 24.3.1 |
| Q2 | postgres:5432 |
| Q3 | 25.8 MB |
| Q4 | 447,671 records |
| Q5 | ✅ Setup complete |

---

**Completed**: 2026-03-17
**Branch**: homework-submissions-2026
