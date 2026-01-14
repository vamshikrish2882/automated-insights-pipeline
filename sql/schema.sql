-- schema.sql
-- Schema definition for the operational analytics sandbox.
-- Creates two core tables:
--   - orders
--   - shipments

PRAGMA foreign_keys = ON;

-- Drop in FK-safe order
DROP TABLE IF EXISTS shipments;
DROP TABLE IF EXISTS orders;

-- ==========================================
-- Orders: customer orders and commercial info
-- ==========================================
CREATE TABLE orders (
    order_id           INTEGER PRIMARY KEY,
    customer_id        INTEGER               NOT NULL,
    order_date         DATE                  NOT NULL,
    required_ship_date DATE                  NOT NULL,
    order_status       TEXT                  NOT NULL, -- SHIPPED | PENDING | CANCELLED
    order_amount       REAL                  NOT NULL,
    priority           TEXT                  NOT NULL, -- LOW | MEDIUM | HIGH
    region             TEXT                  NOT NULL   -- East | West | North | South
);

-- ==========================================
-- Shipments: fulfillment and delivery info
-- ==========================================
CREATE TABLE shipments (
    shipment_id     INTEGER PRIMARY KEY,
    order_id        INTEGER               NOT NULL,
    ship_date       DATE                  NOT NULL,
    delivery_date   DATE                  NOT NULL,
    shipment_status TEXT                  NOT NULL, -- ON_TIME | LATE
    carrier         TEXT                  NOT NULL,
    warehouse_id    INTEGER               NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders (order_id)
);

-- ==========================================
-- Helpful indexes for analytical queries
-- ==========================================
CREATE INDEX IF NOT EXISTS idx_orders_order_date
    ON orders (order_date);

CREATE INDEX IF NOT EXISTS idx_orders_region_priority
    ON orders (region, priority);

CREATE INDEX IF NOT EXISTS idx_shipments_order_id
    ON shipments (order_id);

CREATE INDEX IF NOT EXISTS idx_shipments_delivery_date
    ON shipments (delivery_date);
