from sentence_transformers import CrossEncoder

model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def rerank(query, docs):
    pairs = [(query, doc["text"]) for doc in docs]
    scores = model.predict(pairs)

    for i in range(len(docs)):
        docs[i]["rerank_score"] = float(scores[i])

    return sorted(docs, key=lambda x: x["rerank_score"], reverse=True)