# Automated Insights Pipeline (SQL + Python)

This project demonstrates an **end-to-end automated insights pipeline** for a fictional B2B packaging / operations business.

The goal of the pipeline is to:
- Ingest and clean raw operational data (orders, shipments, inventory)
- Apply SQL-based transformations to create an analytical data model
- Compute business KPIs for operations and fulfillment
- Detect anomalies in on-time shipment performance and revenue
- Output ready-to-use datasets and reports for stakeholders

---

## Tech Stack

- **Languages:** SQL, Python (Pandas)
- **Storage:** CSV files + SQLite database
- **Libraries:** pandas, sqlite3 / SQLAlchemy, matplotlib (for visuals)
- **Design:** Modular, automation-ready pipeline (can be scheduled via Airflow/cron)

---

## Project Structure

```bash
automated-insights-pipeline-daxwell/
  data/
    raw/          # raw input CSVs
    interim/      # intermediate processed files
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
    anomalies.py
    kpis.py
    report.py
  notebooks/
    eda.ipynb
  reports/
    kpi_summary.csv
    anomalies.csv
    figures/
