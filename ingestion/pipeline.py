from llama_index.core.ingestion import IngestionPipeline
from embeddings.gemini_embedding import embed_model
from vector_store.pinecone_store import pinecone_index, upsert_records
from llama_index.vector_stores.pinecone import PineconeVectorStore

vector_store = PineconeVectorStore(pinecone_index=pinecone_index)

pipeline = IngestionPipeline(
    transformations=[embed_model],
    vector_store=vector_store
)

def ingest_data(data):
    embeddings_gemini = [embed_model.get_text_embedding(d["text"]) for d in data]

    records = [
        {
            "id": d["element_id"],
            "values": e,
            "metadata": {"source_text": d["text"], "category": d["type"]}
        }
        for d, e in zip(data, embeddings_gemini)
    ]

    upsert_records(records)
