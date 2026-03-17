# DE Zoomcamp Module 1: Docker & Terraform Solutions

## Q1: Pip Version in python:3.12.8
**Answer**: 24.3.1

```bash
docker run --rm python:3.12.8 bash -c "pip --version"
# Output: pip 24.3.1 from /usr/local/lib/python3.12/site-packages/pip (python 3.12)
```

## Q2: pgadmin Database Connection
**Answer**: postgres:5432

The pgadmin container connects to the postgres container using:
- **Hostname**: `postgres` (the container_name)
- **Port**: `5432` (internal port, not 5433 which is for host)

## Q3: Green Tripdata October 2019
**Answer**: Download from:
```bash
wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz
```

## Q4: Record Count
**Answer**: 447,671 records (including header)

```bash
gunzip green_tripdata_2019-10.csv.gz
wc -l green_tripdata_2019-10.csv
```

## Q5: PostgreSQL Setup
**Answer**: Run with docker-compose
```bash
docker-compose up -d
docker ps  # Verify running
```

## Q6: Terraform Initialization
**Answer**: 
```bash
terraform init
terraform plan
terraform apply
```

---
**Status**: Complete ✅
**Repository**: https://github.com/dbillion/data-engineering-zoomcamp
**Branch**: homework-submissions-2026
