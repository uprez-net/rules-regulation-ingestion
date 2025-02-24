import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API = os.getenv("GOOGLE_API")
PINECONE_API = os.getenv("PINECONE_API_KEY")
LLAMA_KEY = os.getenv("LLAMA_KEY")
INDEX_NAME = "rules-and-regulation"
MODEL_NAME = "models/embedding-001"
