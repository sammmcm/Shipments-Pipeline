CREATE TABLE IF NOT EXISTS shipments (
    shipment_id VARCHAR(50) PRIMARY KEY,
    destination VARCHAR(100) NOT NULL,
    weight_kg NUMERIC(10, 2) NOT NULL,
    status VARCHAR(50) NOT NULL
);