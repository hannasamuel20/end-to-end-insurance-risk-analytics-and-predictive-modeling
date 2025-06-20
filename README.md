# AlphaCare Insurance Solutions (ACIS) — Marketing Analytics Project

## Overview

This project supports AlphaCare Insurance Solutions (ACIS) in developing risk and predictive analytics for car insurance marketing in South Africa. The goal is to analyze historical insurance claim data to optimize marketing strategies and identify “low-risk” customer segments for premium adjustments to attract new clients.

---

## Business Objective

- Analyze historical insurance claim data (Feb 2014 – Aug 2015).
- Identify patterns of risk and profitability across provinces, zip codes, gender, and vehicle types.
- Use statistical and machine learning models to predict total claims and optimize premiums.
- Provide actionable insights to enhance AlphaCare's insurance products and marketing plans.

---

## Project Scope & Deliverables

### Exploratory Data Analysis (EDA) & Statistics
- Understand and summarize the data.
- Detect outliers and trends across geography and time.
- Calculate Loss Ratios and other key financial metrics.
- Visualize data distributions, correlations, and trends.
- Share insights with clear, creative visualizations.

###  Data Version Control (DVC) Pipeline
- Install and initialize DVC for versioning datasets.
- Configure local remote storage for data versioning.
- Track datasets with DVC, commit `.dvc` files to Git.
- Push dataset versions to the local remote storage.
- Ensure reproducible and auditable data workflows.

---

## Project Structure

- `data/` — Contains raw and processed datasets tracked by DVC.
- `notebooks/` — Jupyter notebooks for EDA, statistical analysis, and modeling.
- `src/` — Python scripts and modules for data processing and model training.
- `.dvc/` — DVC metadata and configuration.
- `.github/workflows/` — CI/CD pipeline definitions (GitHub Actions).

---

## Setup Instructions

### Prerequisites

- Python 3.8+
- Git
- DVC (`pip install dvc`)

### Installation & Initialization

```bash
git clone https://github.com/hannasamuel20/end-to-end-insurance-risk-analytics-and-predictive-modeling.git
cd end-to-end-insurance-risk-analytics-and-predictive-modeling

# Initialize Git repository (if not already done)
git init

# Initialize DVC in the project directory
dvc init
