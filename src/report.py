"""
report.py

Generates visualizations from the weekly KPI summary
and saves them to the reports/figures directory.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from .config import KPI_OUTPUT_PATH, FIGURES_DIR, REPORTS_DIR


def generate_plots() -> None:
    """
    Generate revenue, on-time rate, and additional operational plots
    from the weekly KPI summary.
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

    # Ensure sorted by week for consistent plotting
    df = df.sort_values("order_week")

    # -----------------------------
    # 1. Weekly Total Revenue
    # -----------------------------
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

    # -----------------------------
    # 2. Weekly On-Time Shipment Rate
    # -----------------------------
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

    # -----------------------------
    # 3. Weekly Late Shipment Count
    # -----------------------------
    if "late_shipments" in df.columns:
        plt.figure(figsize=(10, 5))
        plt.plot(df["order_week"], df["late_shipments"], marker="o")
        plt.xlabel("Order Week")
        plt.ylabel("Late Shipments")
        plt.title("Weekly Late Shipments Count")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()

        late_plot_path = FIGURES_DIR / "weekly_late_shipments.png"
        plt.savefig(late_plot_path)
        plt.close()
        print(f"Saved late shipments plot to {late_plot_path}")

    # -----------------------------
    # 4. Average Delivery Days Per Week
    # -----------------------------
    if "avg_delivery_days" in df.columns:
        plt.figure(figsize=(10, 5))
        plt.plot(df["order_week"], df["avg_delivery_days"], marker="o")
        plt.xlabel("Order Week")
        plt.ylabel("Average Delivery Days")
        plt.title("Average Delivery Days Per Week")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()

        avg_deliv_path = FIGURES_DIR / "weekly_avg_delivery_days.png"
        plt.savefig(avg_deliv_path)
        plt.close()
        print(f"Saved average delivery days plot to {avg_deliv_path}")

    # -----------------------------
    # 5. Average Days Past Required Date (SLA)
    # -----------------------------
    if "avg_days_past_required" in df.columns:
        plt.figure(figsize=(10, 5))
        plt.plot(df["order_week"], df["avg_days_past_required"], marker="o")
        plt.xlabel("Order Week")
        plt.ylabel("Average Days Past SLA")
        plt.title("Average Days Past Required Date")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()

        avg_sla_path = FIGURES_DIR / "weekly_avg_days_past_required.png"
        plt.savefig(avg_sla_path)
        plt.close()
        print(f"Saved average days past SLA plot to {avg_sla_path}")

    # -----------------------------
    # 6. Revenue vs On-Time Rate (Dual Axis)
    # -----------------------------
    fig, ax1 = plt.subplots(figsize=(10, 5))

    color_left = "tab:blue"
    ax1.set_xlabel("Order Week")
    ax1.set_ylabel("Total Revenue", color=color_left)
    ax1.plot(df["order_week"], df["total_revenue"], color=color_left, marker="o")
    ax1.tick_params(axis="y", labelcolor=color_left)
    ax1.tick_params(axis="x", rotation=45)

    ax2 = ax1.twinx()
    color_right = "tab:green"
    ax2.set_ylabel("On-Time Rate", color=color_right)
    ax2.plot(df["order_week"], df["on_time_rate"], color=color_right, marker="o")
    ax2.tick_params(axis="y", labelcolor=color_right)

    plt.title("Revenue vs On-Time Shipment Rate")
    plt.tight_layout()

    rev_vs_on_time_path = FIGURES_DIR / "revenue_vs_on_time_rate.png"
    plt.savefig(rev_vs_on_time_path)
    plt.close()
    print(f"Saved revenue vs on-time rate plot to {rev_vs_on_time_path}")


def main() -> None:
    generate_plots()


if __name__ == "__main__":
    main()
