# Loan Assistant

## Setup

1. Install dependencies  
   pip install -r requirements.txt

2. Install Playwright browsers  
   playwright install

3. Set environment variables  
   export OPENAI_API_KEY="your_key_here"




Project Setup
Clone the repository and navigate into the project directory:
git clone https://github.com/HarshalSPatil/loan-assitstant.git
cd loan-assistant


Create a Python virtual environment and activate it:
python3 -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate.bat       # Windows


Install dependencies:
pip install -r requirements.txt

Create a .env file at the project root with your API keys:
OPENAI_API_KEY=…       # if using OpenAI
GEMINI_API_KEY=…       # if using Google Gemini


Run the scraper to fetch loan documentation and build your FAISS index:
python src/scrape.py
python src/build_index.py
OR
1. Run the scheduled pipeline (optional)  
   python pipelines/scheduler.py

2. Start the API  
   uvicorn api.main:app --reload

3. Start the Streamlit UI  
   streamlit run frontend/app.py

Architectural Decisions
Libraries
- Playwright for dynamic web scraping of bank portals.
- BeautifulSoup for parsing static HTML segments.
- pandas for intermediate data cleaning and CSV exports.
- FAISS for high-speed vector similarity search.
- finbert-sentence-embedding for finance-tuned embeddings.
- Google GenAI (google-genai) for chat completions with Gemini.
- python-dotenv to manage environment variables securely.
Data Strategy
We chunk loan documents into fixed-length segments with 512/600 tokens and 50% overlap.
- Maintains semantic cohesion across chunks.
- Ensures long paragraphs aren’t split mid–concept.
- Balances search granularity versus index size.

Model Selection
| Component | Model / Tool | Rationale | 
| Embeddings | finbert-sentence-embedding | Captures domain-specific financial terminology | 
| Vector Store | FAISS IndexFlatIP | Inner-product search on normalized vectors for speed | 
| LLM (Chat) | Gemini-1.5-flash | Free, zero-ops, solid general reasoning | 


AI Tools Used
- FinBERT Embedder: local, finance-tuned embeddings without API calls.
- Google Gemini API: free-tier chat model for answer generation.
- RAG Pipeline: custom retrieve() to fetch top-k chunks, then prompt LLM.
- Hugging Face Hub: snapshot_download to cache models for offline use

Challenges Faced
- Dynamic web pages required headless browser automation and manual wait strategies.
- Version mismatches in huggingface_hub broke fname parameters; we pinned to <1.0.0.
- Missing tokenizer errors solved by manually caching FinBERT files and passing model_path.
- Rate-limits on free API tiers handled with exponential backoff in production.



Potential Improvements
- Fine-tune FinBERT on internal loan policy documents for even sharper retrieval.
- Implement hybrid search combining BM25 keyword filters with vector ranking.
- Add a simple web UI to visualize retrieved context and LLM answers.
- Integrate function-calling for structured outputs (tables, loan calculations).
- Quantize embeddings (PQ) to reduce FAISS index footprint on larger corpora. 
- Use of different chunking strategies based on data.


Versioning & Next Steps
Tag releases with semantic versioning and publish to PyPI for easy installation.
Automate nightly data refreshes to keep loan rates and policy changes up to date.
Automate accurate link redirection within scraped data/ improvements in scraping data.



Other:
- We can use azure/other cloud services for search index and openai for better accuracy.








