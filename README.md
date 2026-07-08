# YouTube Trending Data Pipeline & API

This project consists of two main components: a Python script that downloads YouTube trending data from Kaggle and uploads it to Azure Blob Storage, and a FastAPI application that serves this data via RESTful endpoints.

## Overview

1. **Data Pipeline Script:** Connects to Kaggle using `kagglehub`, downloads the `datasnaek/youtube-new` dataset, uploads the Great Britain (`GBvideos.csv`) data to an Azure Blob Storage container with a timestamped filename, and stages a local copy for the API.
2. **FastAPI Application:** Reads the staged CSV data and provides endpoints to query YouTube videos by trending date or video ID.

---

## Prerequisites

Ensure you have Python installed. Install the required dependencies using `pip`:

* `pip install kagglehub[pandas-datasets]`
* `pip install pandas`
* `pip install azure-storage-blob`
* `pip install fastapi`
* `pip install "uvicorn[standard]"`

*Note: You will also need a valid Kaggle account and API token configured on your machine to download the dataset.*

---

## Configuration

Before running the scripts, you need to update a few variables in the data pipeline script to match your environment:

* **File Paths:** Update the hardcoded `C:\Users\OliverWray\...` paths to match your system's dynamic cache path for Kaggle downloads. 
* **Azure Connection String:** Populate the `connection_string = ""` variable with your actual Azure storage account connection string.
* **Azure Container:** Ensure the `container_name = "bob20"` matches your target Azure container.
* **Destination Directory:** The script copies `GBvideos.csv` to `./code/data/CAdata.csv`. Ensure the `./code/data/` directory exists before running the script.

---

## Usage

### Step 1: Run the Data Pipeline

Run the data script to fetch the Kaggle data, upload it to Azure, and stage the local CSV.

```bash
python data_pipeline.py
