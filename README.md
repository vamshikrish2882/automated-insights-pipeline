<p align="center">
  <h1>Automated Insights Pipeline (SQL + Python)</h1>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/SQL-Analytics-blue" />
  <img src="https://img.shields.io/badge/Python-Pandas-green" />
  <img src="https://img.shields.io/badge/ETL-Pipeline-orange" />
  <img src="https://img.shields.io/badge/Automation-Airflow Ready-yellow" />
</p>

This repository contains a **fully automated analytics pipeline** built with SQL and Python that simulates the end-to-end journey of operational analytics — from raw data ingestion to KPI generation, anomaly detection, and visual reporting.

The system processes **50,000+ rows of operational data** (orders and shipments), builds analytical models, computes weekly performance metrics, detects anomalies, and generates reports that can inform business decisions.

---

## 🚀 What This Pipeline Does

The pipeline is designed to mimic real-world analytics engineering workflows used in operations and supply chain teams.

✅ **Generate synthetic operational data**  
✅ **Ingest data into a SQLite analytical store**  
✅ **Transform raw data into a structured analytical model**  
✅ **Compute weekly KPIs for business performance**  
✅ **Detect outlier performance and revenue anomalies**  
✅ **Produce visual reports and CSV summaries**  
✅ **Run the full workflow via a single command**

---

## 🧰 Technology Stack

- **Programming:** Python, SQL  
- **Data Processing:** pandas, NumPy  
- **Storage:** CSV + SQLite  
- **Visualization:** matplotlib  
- **Design:** Modular, automation-ready architecture

---

## 🏗 Project Structure

automated-insights-pipeline/
│
├── data/ # Raw and processed data folders
│ ├── raw/
│ ├── interim/
│ └── processed/
│
├── reports/ # Generated reports & plots
│ ├── kpi_summary.csv
│ ├── anomalies.csv
│ └── figures/
│ ├── weekly_total_revenue.png
│ └── weekly_on_time_rate.png
│
├── sql/ # SQL models & schema
│ ├── schema.sql
│ └── transformations.sql
│
├── src/ # Python ETL + reporting modules
│ ├── config.py
│ ├── db.py
│ ├── generate_data.py
│ ├── extract_load.py
│ ├── transform.py
│ ├── kpis.py
│ ├── anomalies.py
│ ├── report.py
│ └── run_pipeline.py
│
├── requirements.txt
└── README.md
---

## 📊 Pipeline Flow

1. **Data Generation** – Creates synthetic orders & shipment datasets  
2. **Extract & Load** – Loads CSVs into SQLite via schema definitions  
3. **Transform** – Produces an analytical table combining orders + shipments  
4. **KPI Calculation** – Computes weekly operational performance indicators  
5. **Anomaly Detection** – Flags unusual weeks for on‐time rate or revenue  
6. **Reporting & Visualization** – Exports CSV summaries and charts

---

## 📈 Sample Outputs

### KPI Summary
- Weekly on-time shipment rate  
- Total revenue  
- Average delivery time  
- Late shipment count  

Saved to:
reports/kpi_summary.csv

### Anomaly Report
Displays flagged anomalies based on simple statistical thresholds:
reports/anomalies.csv

### Visualizations
- Weekly Total Revenue
- Weekly On-Time Shipment Rate

Saved to: reports/figures/*.png

---

## ✅ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt

2. Run the full pipeline
python -m src.run_pipeline

3. Generate visual reports
python -m src.report


All outputs will be written automatically to the reports/ folder.

💡 Why This Matters

This project showcases:

🔥 End-to-end data pipeline skills
🧠 SQL-based analytical modeling
📊 KPI and anomaly logic for decision support
🛠 ETL and reporting automation design
📦 Clean modular Python architecture

Perfect for demonstrating Data Analyst / Analytics Engineer capabilities.

👤 About the Author

Vamshikrishna Pandilla
Data Analyst • SQL | Python | Analytics Engineering
📧 vamshikrishnapandilla908@gmail.com

🔗 https://www.linkedin.com/in/vamshikrishna-pandilla

Feel free to ask if you want:

✅ A featured project showcase section
✅ Screenshots or embedded images
✅ A demo GIF of pipeline execution
✅ Custom badges (e.g., Python version, license, CI)
