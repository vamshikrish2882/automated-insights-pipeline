"""
transform.py

Runs SQL transformations to build analytical tables/views
from the raw-loaded tables in the SQLite database.
"""

from __future__ import annotations

import sqlite3

from .config import TRANSFORM_SQL_PATH
from .db import get_connection


def run_sql_script(conn: sqlite3.Connection, sql_path) -> None:
    """
    Execute a .sql script file containing one or more SQL statements.
    """
    with open(sql_path, "r", encoding="utf-8") as f:
        sql_script = f.read()

    cursor = conn.cursor()
    cursor.executescript(sql_script)
    conn.commit()


def main() -> None:
    """
    Run the core transformations to create `order_shipments`.
    """
    print("Connecting to database...")
    conn = get_connection()

    try:
        print(f"Running transformations from: {TRANSFORM_SQL_PATH}")
        run_sql_script(conn, TRANSFORM_SQL_PATH)
        print("Transformations completed. 'order_shipments' table created.")
    finally:
        conn.close()
        print("Database connection closed.")


if __name__ == "__main__":
    main()
