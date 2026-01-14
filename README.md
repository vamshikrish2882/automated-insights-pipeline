<p align="center">
  <h2>Automated Insights Pipeline (SQL + Python)</h2>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/SQL-Analytics-blue" />
  <img src="https://img.shields.io/badge/Python-Pandas-green" />
  <img src="https://img.shields.io/badge/ETL-Pipeline-orange" />
  <img src="https://img.shields.io/badge/Automation-Airflow Ready-yellow" />
</p>

This project demonstrates an **end-to-end automated insights pipeline** designed for a fictional B2B operations environment.  
The pipeline automates analytics workflows that would normally take analysts hours each week to manually execute.

The system processes **50,000+ rows of synthetic operational data** (orders + shipments) and produces actionable insights through SQL transformations, Python-based KPI computation, anomaly detection, and automated reporting.

---

## 🌐 **Pipeline Capabilities**

- Ingest and clean raw operational datasets (orders & shipments)
- Build analytical tables using SQL transformations
- Compute weekly business KPIs for operations and fulfillment
- Detect anomalies in on-time shipment performance and revenue
- Generate ready-to-use datasets and visual reports for stakeholders
- Provide a single automated entrypoint to run the entire workflow

---

## 🧰 **Tech Stack**

- **Languages:** SQL, Python (Pandas)
- **Storage:** CSV files + SQLite warehouse
- **Libraries:** pandas, numpy, sqlite3 / SQLAlchemy, matplotlib
- **Design Principles:**  
  - Modular ETL  
  - SQL-first transformations  
  - Automation-ready structure (cron / Airflow friendly)  
  - Clean analytics engineering architecture  

---

## 📁 **Project Structure**

```bash
automated-insights-pipeline/
  data/
    raw/          # raw input CSVs
    interim/      # optional staging files
    processed/    # final cleaned outputs
  sql/
    schema.sql
    transformations.sql
  src/
    config.py
    db.py
    generate_data.py
    extract_load.py
    transform.py
    kpis.py
    anomalies.py
    report.py
    run_pipeline.py
  reports/
    kpi_summary.csv
    anomalies.csv
    figures/
      weekly_total_revenue.png
      weekly_on_time_rate.png
  requirements.txt
  README.md
