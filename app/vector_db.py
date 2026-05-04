from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from app.config import *

client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)

print("✅ vector_db.py LOADED")

def create_collection():
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=VECTOR_SIZE,
            distance=Distance.COSINE
        )
    )

def insert_data(points):
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

def search_vector(query_vector, top_k=5):
    return client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=top_k
    )