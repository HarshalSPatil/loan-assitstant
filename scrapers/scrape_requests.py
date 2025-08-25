import os
import json
import requests
from bs4 import BeautifulSoup
from scrapers.config import sites

def fetch_requests():
    os.makedirs("data/raw", exist_ok=True)
    all_data = []

    for site in sites:
        resp = requests.get(site["url"], timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]

        entry = {
            "site": site["name"],
            "url": site["url"],
            "data": paragraphs
        }
        all_data.append(entry)

    out_path = "data/raw/scraped_requests.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)

    return all_data

if __name__ == "__main__":
    fetch_requests()