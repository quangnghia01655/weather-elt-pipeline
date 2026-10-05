import schedule
import time
import subprocess
import datetime

def run_pipeline():
    print(f"\n[{datetime.datetime.now()}]  Starting Automated Pipeline...")
    
    try:
        # Step 1: Run the Extraction Script
        print(" Running Extract (API to CSV)...")
        subprocess.run(["python", "extract.py"], check=True)
        
        # Step 2: Run dbt Transformation
        print(" Running Transform (dbt to DuckDB)...")
        # Note: If you are using Windows, you might need to use "dbt.cmd" instead of "dbt"
        subprocess.run(["dbt", "run"], check=True)
        
        print(" Pipeline completed successfully!")
    
    except subprocess.CalledProcessError as e:
        print(f" Pipeline failed: {e}")

# Schedule the pipeline to run every day at a specific time (e.g., 8:00 AM)
# For testing right now, you can change it to: schedule.every(1).minutes.do(run_pipeline)
schedule.every().day.at("08:00").do(run_pipeline)

print(" Orchestrator is running. Waiting for scheduled tasks...")

while True:
    schedule.run_pending()
    time.sleep(60)