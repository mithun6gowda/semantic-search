import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

QDRANT_HOST = "localhost"
QDRANT_PORT = 6333

COLLECTION_NAME = "documents"
VECTOR_SIZE = 1536