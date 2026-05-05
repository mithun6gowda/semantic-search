from app.embedding import get_embedding
from app.vector_db import create_collection, insert_data
from qdrant_client.models import PointStruct
import uuid

def chunk_text(text, chunk_size=50, overlap=10):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)

    return chunks

def ingest():
    create_collection()

    with open("data/docs.txt") as f:
        text = f.read()


    chunks = chunk_text(text)

    points = []

    for chunk in chunks:

        vector = get_embedding(chunk)

        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload={"text": chunk}
            )
        )


    insert_data(points)

if __name__ == "__main__":

    ingest()