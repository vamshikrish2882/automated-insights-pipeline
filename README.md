<p align="center">
  <h1>Automated Insights Pipeline (SQL + Python)</h1>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/SQL-Analytics-blue" />
  <img src="https://img.shields.io/badge/Python-Pandas-green" />
  <img src="https://img.shields.io/badge/ETL-Pipeline-orange" />
  <img src="https://img.shields.io/badge/Automation-Airflow Ready-yellow" />
</p>

This repository contains a **fully automated analytics pipeline** built with SQL and Python that simulates the end-to-end journey of operational analytics — from raw data ingestion to KPI computation, anomaly detection, and visual reporting.

The system processes **50,000+ rows of operational data** (orders and shipments), builds analytical models, computes weekly performance metrics, detects anomalies, and generates reports that power data-driven decision making.

---

## 🚀 What This Pipeline Does

This project mirrors real-world analytics engineering workflows used in operations & supply chain teams:

- ✅ Generate synthetic operational datasets  
- ✅ Ingest data into a SQLite analytical store  
- ✅ Build an analytical data model using SQL  
- ✅ Compute weekly KPIs for business performance  
- ✅ Detect revenue & on-time performance anomalies  
- ✅ Produce visual reports and CSV summaries  
- ✅ Run the full workflow with **one command**

---

## 🧰 Technology Stack

- **Languages:** Python, SQL  
- **Processing:** pandas, NumPy  
- **Storage:** CSV + SQLite  
- **Visualization:** matplotlib  
- **Design:** Modular, automation-ready architecture  

---

## 🏗 Project Structure

```bash
automated-insights-pipeline/
│
├── data/                     # Raw and processed data folders
│   ├── raw/
│   ├── interim/
│   └── processed/
│
├── reports/                  # Generated reports & plots
│   ├── kpi_summary.csv
│   ├── anomalies.csv
│   └── figures/
│       ├── weekly_total_revenue.png
│       └── weekly_on_time_rate.png
│
├── sql/                      # SQL models & schema
│   ├── schema.sql
│   └── transformations.sql
│
├── src/                      # Python ETL + analytics modules
│   ├── config.py
│   ├── db.py
│   ├── generate_data.py
│   ├── extract_load.py
│   ├── transform.py
│   ├── kpis.py
│   ├── anomalies.py
│   ├── report.py
│   └── run_pipeline.py
│
├── requirements.txt
└── README.md

