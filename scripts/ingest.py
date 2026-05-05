from app.embedding import get_embedding
from app.vector_db import create_collection, insert_data
from qdrant_client.models import PointStruct
import uuid

def chunk_text(text, chunk_size=300, overlap=50):
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

    print("📄 TEXT LENGTH:", len(text))   # 👈 ADD THIS

    chunks = chunk_text(text)
    print("🧩 CHUNKS:", len(chunks))      # 👈 ADD THIS

    points = []

    for chunk in chunks:
        print("➡️ Processing chunk:", chunk[:50])  # 👈 ADD THIS

        vector = get_embedding(chunk)

        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload={"text": chunk}
            )
        )

    print("📦 POINTS TO INSERT:", len(points))  # 👈 ADD THIS

    insert_data(points)
    print("✅ Data inserted")
if __name__ == "__main__":
    ingest()