from app.embedding import get_embedding
from app.vector_db import search_vector

def semantic_search(query: str, top_k=5):
    query_vector = get_embedding(query)

    results = search_vector(query_vector, top_k)

    return [
        {
            "score": r.score,
            "text": r.payload["text"]
        }
        for r in results
    ]