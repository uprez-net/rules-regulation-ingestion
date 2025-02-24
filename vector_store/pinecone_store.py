from pinecone import Pinecone
from config.settings import PINECONE_API, INDEX_NAME

pc = Pinecone(api_key=PINECONE_API)
pinecone_index = pc.Index(INDEX_NAME)

def upsert_records(records, namespace="new-namespace"):
    pinecone_index.upsert(vectors=records, namespace=namespace)
