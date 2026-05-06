from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from app.config import COLLECTION_NAME, VECTOR_SIZE, QDRANT_HOST, QDRANT_PORT

client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)

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
    response = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=top_k
    )
    return response.points  