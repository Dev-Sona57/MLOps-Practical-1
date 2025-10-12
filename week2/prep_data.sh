#!/usr/bin/env bash
# ==============================
# Data Preparation Script
# ==============================

# Safety flags - these help prevent silent errors
set -euo pipefail

echo "[INFO] Preparing data directory structure..."

# Create data directory
mkdir -p data

# Define the dataset path
RAW_FILE="data/iris.csv"

# Download the dataset from GitHub
echo "[INFO] Downloading dataset..."
curl -L -o $RAW_FILE https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv

# Add a custom row (simulating new data)
echo "custom,0.1,0.2,0.3,setosa" >> $RAW_FILE
echo "[INFO] Added one synthetic row."

# Generate a mini report
LINES=$(wc -l < $RAW_FILE)
echo "[REPORT] Dataset now has $LINES rows."

echo "[INFO] Done!"

