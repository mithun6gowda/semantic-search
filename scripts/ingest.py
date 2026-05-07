import os
import uuid
from app.embedding import get_embedding
from app.vector_db import create_collection, insert_data
from app.pdf_loader import extract_text_from_pdf
from app.web_loader import fetch_text_from_url
from qdrant_client.models import PointStruct

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_DIR = os.path.join(BASE_DIR, "data", "pdfs")

HEALTH_URLS = [
    "https://www.who.int/news-room/fact-sheets/detail/diabetes",
    "https://www.who.int/news-room/fact-sheets/detail/obesity",
    "https://www.cdc.gov/diabetes/basics/diabetes.html",
    "https://www.nhs.uk/conditions/diabetes/"
]

def chunk_text(text, chunk_size=80, overlap=20):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks

def process_text(text, source, source_type, points):
    if not text.strip():
        print(f" Skipping empty source: {source}")
        return

    chunks = chunk_text(text)

    if not chunks:
        print(f" No chunks from: {source}")
        return

    print(f"🧩 Chunks from {source_type}: {len(chunks)}")

    for chunk in chunks:
        vector = get_embedding(chunk)

        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload={
                    "text": chunk,
                    "source": source,
                    "type": source_type
                }
            )
        )

def ingest():
    create_collection()
    points = []

    #  PDF INGESTION
    for file in os.listdir(PDF_DIR):
        if file.endswith(".pdf"):
            path = os.path.join(PDF_DIR, file)

            print(f"\n📄 Processing PDF: {file}")

            text = extract_text_from_pdf(path)

            print(f"📄 Text length: {len(text)}")

            process_text(text, file, "pdf", points)

    #  WEB INGESTION
    for url in HEALTH_URLS:
        print(f"\n🌐 Fetching URL: {url}")

        text = fetch_text_from_url(url)

        print(f"📄 Text length: {len(text)}")

        process_text(text, url, "web", points)

    print(" Total chunks:", len(points))

    if not points:
        print("No valid data extracted. Nothing to insert.")
        return

    insert_data(points)
    print("Data inserted")


if __name__ == "__main__":
    ingest()