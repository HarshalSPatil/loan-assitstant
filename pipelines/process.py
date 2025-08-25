import os
import json

def process_raw():
    os.makedirs("data/processed", exist_ok=True)

    # List of raw file paths
    raw_files = [
        "data/raw/scraped_requests.json",
        "data/raw/scraped_playwright.json"
    ]

    # Initialize variables
    chunks = []
    chunk_size = 600
    idx = 0

    # Recursive function to chunk text
    def chunk_text(words, chunk_size, idx):
        if not words:
            return []
        snippet = " ".join(words[:chunk_size])
        return [{"id": idx, "text": snippet}] + chunk_text(words[chunk_size:], chunk_size, idx + 1)

    # Process each file
    for path in raw_files:
        if not os.path.exists(path):
            continue

        with open(path, "r", encoding="utf-8") as f:
            entries = json.load(f)

        for entry in entries:
            # Combine all text in entry["data"] into a single string
            combined_text = " ".join(entry["data"])
            words = combined_text.split()

            # Use chunk_text to split the combined text into chunks
            chunks.extend(chunk_text(words, chunk_size, idx))
            idx += len(words) // chunk_size + (1 if len(words) % chunk_size > 0 else 0)

    # Write the processed chunks to a file
    out_path = "data/processed/chunks.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)

    print(f"Chunks written to {out_path}")

if __name__ == "__main__":
    process_raw()