from scrapers.config import sites
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import os
import json

def fetch_playwright():
    os.makedirs("data/raw", exist_ok=True)
    all_data = []

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        for site in sites:
            page = browser.new_page()
            page.set_default_timeout(0)  # Disable timeout globally
            # Navigate to the initial URL
            page.goto(site["url"])
            page.wait_for_load_state("networkidle")  # Wait until the network is idle

            # Scrape data from multiple pages (pagination)
            while True:
                # Get the current page's content
                html = page.content()
                soup = BeautifulSoup(html, "html.parser")
                paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]

                # Add the data to the entry
                entry = {
                    "site": site["name"],
                    "url": page.url,  # Capture the current URL (handles redirects)
                    "data": paragraphs
                }
                all_data.append(entry)

                # Check for a "Next" button or pagination link
                try:
                    next_button = page.locator("text=Next")  # Adjust selector if needed
                    if next_button.is_visible():
                        next_button.click()
                        page.wait_for_load_state("networkidle")  # Wait for the next page to load
                    else:
                        break  # No more pages
                except:
                    break  # Exit loop if "Next" button is not found or fails

        browser.close()

    # Save the scraped data to a JSON file
    out_path = "data/raw/scraped_playwright.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)