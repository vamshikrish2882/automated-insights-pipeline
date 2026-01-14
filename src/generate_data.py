"""
generate_data.py

Generates synthetic operational data for:
- orders
- shipments

and saves them as CSVs in data/raw/.
"""

from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path
from typing import List

import numpy as np
import pandas as pd

from .config import RAW_DATA_DIR

N_ORDERS = 50_000
START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2024, 12, 31)


def random_dates(n: int, start: datetime, end: datetime) -> List[datetime]:
    """
    Generate n random dates between start and end.
    """
    delta_days = (end - start).days
    offsets = np.random.randint(0, delta_days + 1, size=n)
    return [start + timedelta(days=int(d)) for d in offsets]


def generate_orders() -> pd.DataFrame:
    """
    Generate synthetic order data.
    """
    np.random.seed(42)

    order_ids = np.arange(1, N_ORDERS + 1)
    customer_ids = np.random.randint(1000, 2000, size=N_ORDERS)

    order_dates = random_dates(N_ORDERS, START_DATE, END_DATE)
    required_ship_dates = [
        od + timedelta(days=int(offset))
        for od, offset in zip(order_dates, np.random.randint(1, 6, size=N_ORDERS))
    ]

    regions = np.random.choice(
        ["East", "West", "North", "South"],
        size=N_ORDERS,
        p=[0.3, 0.3, 0.2, 0.2],
    )

    priorities = np.random.choice(
        ["LOW", "MEDIUM", "HIGH"],
        size=N_ORDERS,
        p=[0.4, 0.4, 0.2],
    )

    base_amounts = np.random.lognormal(mean=3.5, sigma=0.5, size=N_ORDERS)
    priority_multiplier = np.where(priorities == "HIGH", 1.3, 1.0)
    order_amounts = np.round(base_amounts * priority_multiplier, 2)

    order_statuses = np.random.choice(
        ["SHIPPED", "PENDING", "CANCELLED"],
        size=N_ORDERS,
        p=[0.8, 0.15, 0.05],
    )

    orders_df = pd.DataFrame(
        {
            "order_id": order_ids,
            "customer_id": customer_ids,
            "order_date": [d.date() for d in order_dates],
            "required_ship_date": [d.date() for d in required_ship_dates],
            "order_status": order_statuses,
            "order_amount": order_amounts,
            "priority": priorities,
            "region": regions,
        }
    )

    return orders_df


def generate_shipments(orders_df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate shipments for a subset of shipped orders.
    """
    np.random.seed(43)

    shipped_orders = orders_df[orders_df["order_status"] == "SHIPPED"].copy()

    # About 95% of shipped orders get shipment records
    has_shipment_mask = np.random.rand(len(shipped_orders)) < 0.95
    shipped_orders = shipped_orders[has_shipment_mask]

    n_shipments = len(shipped_orders)
    shipment_ids = np.arange(1, n_shipments + 1)

    ship_offsets = np.random.randint(0, 4, size=n_shipments)  # 0–3 days after order_date
    ship_dates = [
        order_date + timedelta(days=int(offset))
        for order_date, offset in zip(shipped_orders["order_date"], ship_offsets)
    ]

    delivery_offsets = np.random.randint(1, 8, size=n_shipments)
    delivery_dates = [
        ship_date + timedelta(days=int(offset))
        for ship_date, offset in zip(ship_dates, delivery_offsets)
    ]

    required_dates = shipped_orders["required_ship_date"].tolist()
    is_late = [int(dd > rd) for dd, rd in zip(delivery_dates, required_dates)]

    shipment_statuses = np.where(np.array(is_late) == 1, "LATE", "ON_TIME")

    carriers = np.random.choice(["CarrierA", "CarrierB", "CarrierC"], size=n_shipments)
    warehouse_ids = np.random.randint(1, 6, size=n_shipments)

    shipments_df = pd.DataFrame(
        {
            "shipment_id": shipment_ids,
            "order_id": shipped_orders["order_id"].values,
            "ship_date": ship_dates,
            "delivery_date": delivery_dates,
            "shipment_status": shipment_statuses,
            "carrier": carriers,
            "warehouse_id": warehouse_ids,
        }
    )

    shipments_df["ship_date"] = pd.to_datetime(shipments_df["ship_date"]).dt.date
    shipments_df["delivery_date"] = pd.to_datetime(shipments_df["delivery_date"]).dt.date

    return shipments_df


def main() -> None:
    """
    Generate orders and shipments CSVs under data/raw/.
    """
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    print("Generating orders data...")
    orders_df = generate_orders()

    print("Generating shipments data...")
    shipments_df = generate_shipments(orders_df)

    orders_path = RAW_DATA_DIR / "orders.csv"
    shipments_path = RAW_DATA_DIR / "shipments.csv"

    orders_df.to_csv(orders_path, index=False)
    shipments_df.to_csv(shipments_path, index=False)

    print(f"Saved orders to {orders_path} ({len(orders_df)} rows)")
    print(f"Saved shipments to {shipments_path} ({len(shipments_df)} rows)")


if __name__ == "__main__":
    main()
