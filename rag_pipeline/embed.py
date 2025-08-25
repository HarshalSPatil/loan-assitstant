import os
from finbert_embedding.embedding import FinbertEmbedding
# from huggingface_hub import snapshot_download

# Ensure the models directory exists
# snapshot_download(
#     repo_id="ProsusAI/finbert",
#     cache_dir="./models/finbert",
#     local_dir="./models/finbert",
#     local_dir_use_symlinks=False
# )

# Initialize the FinBERT embedder (downloads model on first run)
finbert = FinbertEmbedding(model_path="./models/finbert")



def get_embedding(text: str) -> list[float]:
    """
    Generate a 768-dimensional sentence embedding for `text`
    using FinBERT’s finance-tuned model.
    """
    embedding = finbert.sentence_vector(text)
    return embedding.tolist() # Convert numpy array to list

# Uncomment the following lines if you want to use OpenAI's API for embeddings 
# import openai
# from dotenv import load_dotenv

# # Load the .env file
# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

# def get_embedding(text: str) -> list:
#     response = openai.Embedding.create(
#         input=text,
#         model="text-embedding-ada-002"
#     )
#     return response["data"][0]["embedding"]