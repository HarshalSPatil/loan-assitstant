import json
import faiss
import numpy as np
from rag_pipeline.embed import get_embedding

_index = None
_texts = []

def _load_index():
    global _index, _texts
    if _index is None:
        _index = faiss.read_index("data/processed/faiss.index")
        with open("data/processed/texts.json", "r", encoding="utf-8") as f:
            _texts = json.load(f)
    return _index, _texts

def retrieve(query: str, top_k: int = 5) -> list:
    index, texts = _load_index()
    q_vec = np.array([get_embedding(query)], dtype="float32")
    distances, indices = index.search(q_vec, top_k)
    return [texts[i] for i in indices[0]]