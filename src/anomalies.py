"""
anomalies.py

Identifies anomalous weeks based on KPI metrics and writes
the results to an anomalies CSV.
"""

from __future__ import annotations

import pandas as pd

from .config import KPI_OUTPUT_PATH, ANOMALIES_OUTPUT_PATH, REPORTS_DIR


def detect_anomalies() -> pd.DataFrame:
    """
    Detect anomalous weeks using simple z-score thresholds
    on on-time rate and total revenue.
    """
    if not KPI_OUTPUT_PATH.exists():
        raise FileNotFoundError(
            f"KPI summary not found at {KPI_OUTPUT_PATH}. "
            "Run kpis.py or the full pipeline first."
        )

    df = pd.read_csv(KPI_OUTPUT_PATH)

    if df.empty:
        print("KPI summary is empty. No anomalies to detect.")
        return pd.DataFrame()

    on_time_mean = df["on_time_rate"].mean()
    on_time_std = df["on_time_rate"].std(ddof=0)

    revenue_mean = df["total_revenue"].mean()
    revenue_std = df["total_revenue"].std(ddof=0)

    if on_time_std == 0:
        df["on_time_z"] = 0.0
    else:
        df["on_time_z"] = (df["on_time_rate"] - on_time_mean) / on_time_std

    if revenue_std == 0:
        df["revenue_z"] = 0.0
    else:
        df["revenue_z"] = (df["total_revenue"] - revenue_mean) / revenue_std

    on_time_anomaly = df["on_time_z"] < -1.5
    revenue_high_anomaly = df["revenue_z"] > 2.0
    revenue_low_anomaly = df["revenue_z"] < -2.0

    df["is_on_time_anomaly"] = on_time_anomaly
    df["is_revenue_high_anomaly"] = revenue_high_anomaly
    df["is_revenue_low_anomaly"] = revenue_low_anomaly

    anomalies_df = df[on_time_anomaly | revenue_high_anomaly | revenue_low_anomaly].copy()

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    anomalies_df.to_csv(ANOMALIES_OUTPUT_PATH, index=False)

    print(f"Detected {len(anomalies_df)} anomalous weeks.")
    print(f"Anomalies written to {ANOMALIES_OUTPUT_PATH}")

    return anomalies_df


def main() -> None:
    anomalies_df = detect_anomalies()
    if anomalies_df.empty:
        print("No anomalies detected.")
    else:
        print("Sample anomalies:")
        print(
            anomalies_df[
                [
                    "order_week",
                    "on_time_rate",
                    "total_revenue",
                    "is_on_time_anomaly",
                    "is_revenue_high_anomaly",
                    "is_revenue_low_anomaly",
                ]
            ].head()
        )


if __name__ == "__main__":
    main()
