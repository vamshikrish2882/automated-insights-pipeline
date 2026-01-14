"""
config.py

Central configuration for file paths and database settings.
"""

import os
from pathlib import Path

# Base directory (root of the project)
BASE_DIR = Path(__file__).resolve().parent.parent

# Data directories
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# SQL directory
SQL_DIR = BASE_DIR / "sql"

# Database path (SQLite)
DB_PATH = DATA_DIR / "insights.db"

# SQL files
SCHEMA_SQL_PATH = SQL_DIR / "schema.sql"
TRANSFORM_SQL_PATH = SQL_DIR / "transformations.sql"

# Reports / outputs
REPORTS_DIR = BASE_DIR / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

KPI_OUTPUT_PATH = REPORTS_DIR / "kpi_summary.csv"
ANOMALIES_OUTPUT_PATH = REPORTS_DIR / "anomalies.csv"
