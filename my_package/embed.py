# my_package/embed.py
from typing import List
# from sentence_transformers import SentenceTransformer
from .data_models import Chunk

class Embedder:
    def __init__(self, model_name: str = 'distilbert-base-nli-stsb-mean-tokens'):
        # self.model = SentenceTransformer(model_name)
        return

    def embed(self, chunks: List[Chunk]) -> List[Chunk]:
        return chunks
        texts = [chunk.text for chunk in chunks]
        embeddings = self.model.encode(texts)
        for chunk, embedding in zip(chunks, embeddings):
            chunk.embedding = embedding
        return chunks
