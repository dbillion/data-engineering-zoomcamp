#!/bin/bash
# DE Zoomcamp Module 1: Docker & Terraform Setup

echo "=== DATA ENGINEERING ZOOMCAMP - MODULE 1 SETUP ==="

# Check Docker
echo -e "\n1. Checking Docker..."
if command -v docker &> /dev/null; then
    docker --version
    echo "✅ Docker is installed"
else
    echo "❌ Docker not found - install from https://docs.docker.com/get-docker/"
fi

# Check Docker Compose
echo -e "\n2. Checking Docker Compose..."
if command -v docker-compose &> /dev/null; then
    docker-compose --version
    echo "✅ Docker Compose is installed"
else
    echo "❌ Docker Compose not found"
fi

# Check Terraform
echo -e "\n3. Checking Terraform..."
if command -v terraform &> /dev/null; then
    terraform --version
    echo "✅ Terraform is installed"
else
    echo "❌ Terraform not found - install from https://developer.hashicorp.com/terraform/install"
fi

# Check Python
echo -e "\n4. Checking Python..."
python3 --version

# Check GCP CLI
echo -e "\n5. Checking gcloud CLI..."
if command -v gcloud &> /dev/null; then
    gcloud --version | head -1
    echo "✅ gcloud CLI is installed"
else
    echo "❌ gcloud CLI not found - install from https://cloud.google.com/sdk/docs/install"
fi

echo -e "\n=== SETUP COMPLETE ==="
echo "Next: Run docker-compose up -d in module folder"
