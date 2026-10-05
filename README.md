🌤️ Automated ELT Weather Data Pipeline

📝 Overview

This project is an end-to-end Automated ELT (Extract, Load, Transform) data pipeline. It extracts daily weather data from a REST API, loads it into local storage, transforms and cleans the data using dbt, and visualizes the final metrics using Streamlit.

The project demonstrates a modern, localized Data Engineering stack using DuckDB as a fast, serverless analytical data warehouse, fully automated via Python scheduling.

🛠️ Tech Stack

Data Extraction & Orchestration: Python (requests, pandas, schedule, subprocess)

Data Warehouse: DuckDB (Local analytical database)

Data Transformation: dbt (Data Build Tool)

Data Visualization: Streamlit

API Source: OpenWeatherMap API

🏗️ Pipeline Architecture

Extract & Load: A Python script queries the OpenWeatherMap API for multiple global cities, extracts current weather conditions, and saves the raw data as CSV files.

Transform: dbt connects to DuckDB, reads the raw CSV files, and applies SQL transformations. This includes casting data types, handling null values, and dynamically converting temperature metrics from Kelvin to Celsius.

Orchestrate: A Python orchestrator script runs continuously in the background, scheduling the extraction and transformation steps to run sequentially every day at a specified time.

Visualize: A Streamlit web application connects directly to the DuckDB warehouse to query the transformed data and display interactive KPIs and charts.

🚀 How to Run the Project

Prerequisites

Python 3.8+

An API key from OpenWeatherMap

1. Setup Environment

Clone the repository and install the required Python packages:

pip install requests pandas dbt-duckdb streamlit schedule


Update the API_KEY variable in extract.py with your OpenWeatherMap key (never upload your real key to GitHub!).

2. Run the Automated Orchestrator

Instead of running steps manually, start the orchestrator to manage the pipeline:

python orchestrator.py


(By default, this will run the extraction and dbt transformation daily at 08:00 AM. You can modify the script to run every minute for testing purposes).

3. Launch the Dashboard

In a separate terminal window, run the Streamlit application to view the interactive dashboard:

streamlit run dashboard.py


