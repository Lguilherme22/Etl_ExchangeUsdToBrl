CREATE TABLE IF NOT EXISTS exchange_usd_rates (
    description VARCHAR,
    datetime TIMESTAMP,
    float_rate FLOAT
);


CREATE TABLE IF NOT EXISTS exchange_real_rates (
    description_coin VARCHAR(50),
    datetime_rate TIMESTAMP,
    float_rate FLOAT,
    etl_created_at TIMESTAMP,
    etl_updated_at TIMESTAMP
);
