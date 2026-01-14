"""
kpis.py

Computes weekly KPIs from the 'order_shipments' analytical table
and writes them to a CSV in the reports directory.
"""

from __future__ import annotations

import pandas as pd

from .config import KPI_OUTPUT_PATH, REPORTS_DIR
from .db import get_connection


def compute_weekly_kpis() -> pd.DataFrame:
    """
    Compute weekly KPIs grouped by order_week.
    """
    conn = get_connection()

    query = """
        SELECT
            order_week,
            COUNT(*) AS total_orders,
            SUM(CASE WHEN shipment_status IS NOT NULL THEN 1 ELSE 0 END) AS shipped_orders,
            SUM(CASE WHEN shipment_status IS NOT NULL AND is_late_flag = 0 THEN 1 ELSE 0 END) AS on_time_shipments,
            SUM(CASE WHEN is_late_flag = 1 THEN 1 ELSE 0 END) AS late_shipments,
            SUM(order_amount) AS total_revenue,
            AVG(order_to_delivery_days) AS avg_delivery_days,
            AVG(CASE WHEN is_late_flag = 1 THEN days_past_required ELSE NULL END) AS avg_days_past_required
        FROM order_shipments
        GROUP BY order_week
        ORDER BY order_week;
    """

    df = pd.read_sql_query(query, conn)
    conn.close()

    def safe_on_time_rate(row) -> float | None:
        shipped = row["shipped_orders"]
        if shipped and shipped > 0:
            return row["on_time_shipments"] / shipped
        return None

    df["on_time_rate"] = df.apply(safe_on_time_rate, axis=1)

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(KPI_OUTPUT_PATH, index=False)
    print(f"Weekly KPIs written to {KPI_OUTPUT_PATH}")

    return df


def main() -> None:
    df = compute_weekly_kpis()
    print("Sample of KPI summary:")
    print(df.head())


if __name__ == "__main__":
    main()
