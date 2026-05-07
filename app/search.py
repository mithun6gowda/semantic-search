from app.embedding import get_embedding
from app.vector_db import search_vector
from app.reranker import rerank

def semantic_search(query: str, top_k=5):
    query_vector = get_embedding(query)

    results = search_vector(query_vector, top_k=10)

    docs = [
        {"text": p.payload.get("text", ""), "score": p.score}
        for p in results
    ]

    reranked = rerank(query, docs)

    return [
    {
        "text": doc["text"],
        "score": round(doc["rerank_score"], 3)
    }
    for doc in reranked[:top_k]
    ]