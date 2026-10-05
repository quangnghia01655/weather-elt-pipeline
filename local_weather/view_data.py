import duckdb

# Connect to the DuckDB database (it will create the database file if it doesn't exist)
conn = duckdb.connect('weather_warehouse.duckdb')

# Display the data in a table
print("--- List of tables in the database ---")
print(conn.execute("SHOW ALL TABLES").df())

# Try to query the stg_daily_weather table and display the data
try:
    df = conn.execute("SELECT * FROM main.stg_daily_weather").df()
    print("\n--- Your data ---")
    print(df)
except Exception as e:
    print(f"\nError: {e}")