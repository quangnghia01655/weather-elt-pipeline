{{ config(materialized='table') }}

SELECT
    city,
    country,
    CAST(temperature AS DOUBLE) AS temp_celsius,
    CAST(humidity AS INTEGER) AS humidity_pct,
    CAST(wind_speed AS DOUBLE) AS wind_speed_mps,
    LOWER(weather_condition) AS condition_desc,
    CAST(extraction_date AS TIMESTAMP) AS extracted_at
FROM read_csv_auto('../data/raw/*.csv') 
WHERE city IS NOT NULL