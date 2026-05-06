from app.embedding import get_embedding
from app.vector_db import search_vector

def semantic_search(query: str, top_k=5):
    query_vector = get_embedding(query)

    results = search_vector(query_vector, top_k)

    return [
        {
            "score": point.score,
            "text": point.payload.get("text", "")
        }
        for point in results
    ]