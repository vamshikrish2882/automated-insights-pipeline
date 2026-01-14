"""
db.py

Database helper functions for connecting to SQLite and initializing schema.
"""

import sqlite3
from pathlib import Path
from typing import Optional

from .config import DB_PATH, SCHEMA_SQL_PATH


def get_connection(db_path: Optional[Path] = None) -> sqlite3.Connection:
    """
    Create a SQLite connection and enable foreign key constraints.
    """
    path = db_path or DB_PATH
    conn = sqlite3.connect(path.as_posix())
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def initialize_schema(conn: sqlite3.Connection, schema_path: Path = SCHEMA_SQL_PATH) -> None:
    """
    Initialize database schema by executing schema.sql.
    Drops and recreates tables each time this is called.
    """
    with open(schema_path, "r", encoding="utf-8") as f:
        schema_sql = f.read()

    cursor = conn.cursor()
    cursor.executescript(schema_sql)
    conn.commit()
