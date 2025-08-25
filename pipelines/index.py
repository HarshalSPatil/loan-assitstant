import os
import json
import faiss
import numpy as np
from rag_pipeline.embed import get_embedding

def build_index():
    os.makedirs("data/processed", exist_ok=True)
    chunks_path = "data/processed/chunks.json"

    if not os.path.exists(chunks_path):
        raise FileNotFoundError("Run pipelines/process.py first.")

    with open(chunks_path, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    # determine embedding dimension
    dim = len(get_embedding("test"))
    print(f"Embedding dimension: {dim}")
    index = faiss.IndexFlatL2(dim)
    texts = []

    for chunk in chunks:
        emb = get_embedding(chunk["text"])
        index.add(np.array([emb], dtype="float32"))
        texts.append(chunk["text"])

    faiss.write_index(index, "data/processed/faiss.index")
    with open("data/processed/texts.json", "w", encoding="utf-8") as f:
        json.dump(texts, f, ensure_ascii=False, indent=2)

    return index

if __name__ == "__main__":
    build_index()