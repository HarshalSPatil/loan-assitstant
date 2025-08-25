import time
import schedule

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# print("Python Path:", sys.path)
from scrapers.scrape_requests import fetch_requests
from scrapers.scrape_playwright import fetch_playwright
from pipelines.process import process_raw
from pipelines.index import build_index
def job():
    fetch_requests()
    print("Requests fetched successfully.")
    fetch_playwright()
    print("Playwright data fetched successfully.")
    process_raw()
    print("Raw data processed successfully.")
    build_index()
    print("Pipeline run complete.")

if __name__ == "__main__":
    # Run immediately, then once a day at midnight
    job()
    schedule.every().day.at("00:00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(60)