from fastapi import FastAPI
from app.search import semantic_search

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API running"}

@app.get("/search")
def search(query: str):
    return {"results": semantic_search(query)}