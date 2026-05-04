from fastapi import FastAPI
from app.search import semantic_search

app = FastAPI()

@app.get("/search")
def search(query: str):
    results = semantic_search(query)
    return {"results": results}