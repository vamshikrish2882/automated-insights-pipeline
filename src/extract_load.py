"""
extract_load.py

ETL step: Load raw CSV data into the SQLite database using the predefined schema.
"""

from __future__ import annotations

import pandas as pd

from .config import RAW_DATA_DIR
from .db import get_connection, initialize_schema


def load_csv_to_table(conn, csv_filename: str, table_name: str) -> None:
    """
    Load a CSV file (in RAW_DATA_DIR) into a SQLite table.
    """
    csv_path = RAW_DATA_DIR / csv_filename

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    df = pd.read_csv(csv_path)

    if df.empty:
        print(f"[WARN] {csv_path} is empty. No rows loaded into {table_name}.")
        return

    df.to_sql(table_name, conn, if_exists="append", index=False)
    print(f"Loaded {len(df)} rows into '{table_name}' from {csv_path}")


def main() -> None:
    """
    Initialize schema and load orders & shipments into SQLite.
    """
    print("Connecting to database...")
    conn = get_connection()

    try:
        print("Initializing schema...")
        initialize_schema(conn)

        print("Loading orders.csv into 'orders' table...")
        load_csv_to_table(conn, "orders.csv", "orders")

        print("Loading shipments.csv into 'shipments' table...")
        load_csv_to_table(conn, "shipments.csv", "shipments")

        print("Extract & Load completed successfully.")
    finally:
        conn.close()
        print("Database connection closed.")


if __name__ == "__main__":
    main()
