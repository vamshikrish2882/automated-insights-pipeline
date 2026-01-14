
<p align="center">
  <h1>Automated Insights Pipeline (SQL + Python)</h1>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/SQL-Analytics-blue" />
  <img src="https://img.shields.io/badge/Python-Pandas-green" />
  <img src="https://img.shields.io/badge/ETL-Pipeline-orange" />
  <img src="https://img.shields.io/badge/Automation-Airflow Ready-yellow" />
</p>

This project showcases an **end-to-end automated insights pipeline** designed for a fictional operations and fulfillment dataset.  
It processes **50,000+ synthetic order and shipment records**, applies SQL transformations, computes weekly KPIs, detects anomalies, and generates visual reports that support real-world decision making.

The goal of this project is to demonstrate how data analysts and analytics engineers can build reliable, modular, and automation-ready analytics workflows using **Python, SQL, and Pandas**.

---

## 🚀 What This Pipeline Does

This pipeline replicates the type of analytical workflows commonly used across operations, supply chain, and fulfillment teams.

It automatically performs:

- **Data Generation** – creates 50K+ rows of realistic operational data  
- **Extract & Load** – ingests raw CSVs into a SQLite “analytics store”  
- **SQL Transformations** – builds a clean analytical data model (`order_shipments`)  
- **KPI Calculations** – computes weekly metrics like on-time rate and revenue  
- **Anomaly Detection** – flags unusual performance and revenue fluctuations  
- **Automated Reporting** – generates CSV outputs and time-series charts  
- **One-click Pipeline Execution** – run everything using one command

---

## 🧰 Technology Stack

- **Python:** pandas, numpy, matplotlib  
- **SQL:** SQLite + SQL analytical modeling  
- **File Formats:** CSV  
- **Design Principles:** modular code, reproducible workflows, Airflow-ready structure  

---

## 🗂 Project Structure

```
automated-insights-pipeline/
│
├── data/                     
│   ├── raw/                  # raw input data files
│   ├── interim/              # optional staging files
│   └── processed/            # cleaned & final outputs
│
├── reports/                  
│   ├── kpi_summary.csv       # generated weekly KPIs
│   ├── anomalies.csv         # anomaly detection results
│   └── figures/              # time-series plots
│       ├── weekly_total_revenue.png
│       └── weekly_on_time_rate.png
│
├── sql/
│   ├── schema.sql            # database schema
│   └── transformations.sql   # analytical model creation
│
├── src/
│   ├── config.py             # path & configuration settings
│   ├── db.py                 # SQLite helpers
│   ├── generate_data.py      # synthetic data generator
│   ├── extract_load.py       # CSV → SQLite loader
│   ├── transform.py          # runs SQL transformations
│   ├── kpis.py               # computes weekly metrics
│   ├── anomalies.py          # outlier/anomaly detector
│   ├── report.py             # generates visual charts
│   └── run_pipeline.py       # orchestrates entire pipeline
│
├── requirements.txt
└── README.md
```

---

## 📊 Pipeline Flow

### 1. **Data Generation**  
Creates synthetic operational datasets (orders + shipments).

### 2. **Extract & Load**  
Imports raw CSV files into a SQLite database defined by `schema.sql`.

### 3. **SQL Transformations**  
Creates the consolidated analytical table `order_shipments`, including:

- delivery lead time  
- days past required date  
- late shipment flag  
- weekly grouping (`order_week`)  

### 4. **KPI Calculation**  
Outputs weekly performance metrics such as:

- on-time shipment rate  
- total revenue  
- late shipment count  
- average delivery duration  
- average SLA delay  

### 5. **Anomaly Detection**  
Flags unusual weeks using simple z-score thresholds:

- ⚠️ abnormal performance  
- 📉 revenue drops  
- 📈 revenue spikes  

### 6. **Reporting & Visualization**  
Exports:

- `reports/kpi_summary.csv`  
- `reports/anomalies.csv`  
- Time-series performance charts  

---

## 📈 Sample Outputs

### 📄 KPI Summary
File location:
```
reports/kpi_summary.csv
```

Includes:
```
- On-time shipment rate
- Total weekly revenue
- Late shipment count
- Avg. delivery days
- Avg. days past required date
```

---

### 🚨 Anomaly Report
File location:
```
reports/anomalies.csv
```

Flags:
```
- ⚠️ Low on-time performance
- 📉 Revenue declines
- 📈 Revenue spikes
```

---

### 🖼 Visual Reports
Saved in:
```
reports/figures/
```

Files:
```
- weekly_total_revenue.png
- weekly_on_time_rate.png
```

---

## ▶️ How to Run the Pipeline

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the entire pipeline
```bash
python -m src.run_pipeline
```

### 3. Generate visual reports
```bash
python -m src.report
```

All generated outputs appear in the **reports/** directory.

---

## 💡 Why This Project Matters

This automated insights pipeline demonstrates key industry skills:

- End-to-end ETL & data modeling  
- SQL-based analytical transformations  
- KPI design for operations  
- Anomaly detection logic  
- Automated reporting with Python  
- Modular, production-ready project structure  

A strong portfolio project for **Data Analyst, Analytics Engineer, or Data Engineering** roles.

---

## 👤 About the Author

**Vamshikrishna Pandilla**  
Data Analyst • SQL • Python • Analytics Engineering  
📧 Email: vamshikrishnapandilla908@gmail.com  
🔗 LinkedIn: https://www.linkedin.com/in/vamshikrishna-pandilla
