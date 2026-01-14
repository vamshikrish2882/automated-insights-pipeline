"""
report.py

Generates simple visualizations from the weekly KPI summary
and saves them to the reports/figures directory.
"""

from __future__ import annotations

import pandas as pd
import matplotlib.pyplot as plt

from .config import KPI_OUTPUT_PATH, FIGURES_DIR, REPORTS_DIR


def generate_plots() -> None:
    """
    Generate revenue and on-time rate plots from KPI summary.
    """
    if not KPI_OUTPUT_PATH.exists():
        raise FileNotFoundError(
            f"KPI summary not found at {KPI_OUTPUT_PATH}. "
            "Run the pipeline or kpis.py first."
        )

    df = pd.read_csv(KPI_OUTPUT_PATH)
    if df.empty:
        print("KPI summary is empty. No plots to generate.")
        return

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    df = df.sort_values("order_week")

    # Revenue plot
    plt.figure(figsize=(10, 5))
    plt.plot(df["order_week"], df["total_revenue"])
    plt.xlabel("Order Week")
    plt.ylabel("Total Revenue")
    plt.title("Weekly Total Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()

    revenue_plot_path = FIGURES_DIR / "weekly_total_revenue.png"
    plt.savefig(revenue_plot_path)
    plt.close()
    print(f"Saved revenue plot to {revenue_plot_path}")

    # On-time rate plot
    plt.figure(figsize=(10, 5))
    plt.plot(df["order_week"], df["on_time_rate"])
    plt.xlabel("Order Week")
    plt.ylabel("On-Time Shipment Rate")
    plt.title("Weekly On-Time Shipment Rate")
    plt.xticks(rotation=45)
    plt.tight_layout()

    on_time_plot_path = FIGURES_DIR / "weekly_on_time_rate.png"
    plt.savefig(on_time_plot_path)
    plt.close()
    print(f"Saved on-time rate plot to {on_time_plot_path}")


def main() -> None:
    generate_plots()


if __name__ == "__main__":
    main()
