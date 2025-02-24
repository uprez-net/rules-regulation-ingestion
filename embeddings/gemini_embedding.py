from llama_index.embeddings.gemini import GeminiEmbedding
from config.settings import GOOGLE_API, MODEL_NAME

embed_model = GeminiEmbedding(model_name=MODEL_NAME, api_key=GOOGLE_API)
