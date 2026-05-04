# from openai import OpenAI
# from app.config import OPENAI_API_KEY

# def get_client():
#     return OpenAI(api_key=OPENAI_API_KEY)

# def get_embedding(text: str):
#     client = get_client()

#     response = client.embeddings.create(
#         model="text-embedding-3-small",
#         input=text
#     )

#     return response.data[0].embedding


from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text: str):
    return model.encode(text).tolist()