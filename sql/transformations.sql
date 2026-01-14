-- transformations.sql
-- Builds the core analytical table `order_shipments`
-- by joining orders and shipments and computing derived metrics
-- used for KPIs and anomaly detection.

PRAGMA foreign_keys = ON;

-- Rebuild analytical table on each pipeline run
DROP TABLE IF EXISTS order_shipments;

CREATE TABLE order_shipments AS
SELECT
    -- Core order attributes
    o.order_id,
    o.customer_id,
    o.order_date,
    o.required_ship_date,
    o.order_status,
    o.order_amount,
    o.priority,
    o.region,

    -- Shipment attributes (may be NULL when not yet shipped)
    s.shipment_id,
    s.ship_date,
    s.delivery_date,
    s.shipment_status,
    s.carrier,
    s.warehouse_id,

    -- Time bucket for weekly KPIs (YYYY-weekNumber)
    strftime('%Y-%W', o.order_date) AS order_week,

    -- Days between required ship date and actual delivery (lateness)
    CASE
        WHEN s.delivery_date IS NULL THEN NULL
        ELSE julianday(s.delivery_date) - julianday(o.required_ship_date)
    END AS days_past_required,

    -- Days from order creation to delivery (customer lead time)
    CASE
        WHEN s.delivery_date IS NULL THEN NULL
        ELSE julianday(s.delivery_date) - julianday(o.order_date)
    END AS order_to_delivery_days,

    -- Late flag: 1 if delivered after required_ship_date, else 0
    CASE
        WHEN s.delivery_date IS NULL THEN 0
        WHEN s.delivery_date > o.required_ship_date THEN 1
        ELSE 0
    END AS is_late_flag

FROM orders o
LEFT JOIN shipments s
    ON o.order_id = s.order_id;
