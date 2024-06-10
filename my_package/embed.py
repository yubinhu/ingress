# my_package/embed.py
from typing import List
from .data_models import Chunk
from openai import OpenAI

client = OpenAI()

def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding

class Embedder:
    def __init__(self, model_name: str = 'text-embedding-3-small'):
        self.model_name = model_name

    def embed(self, chunks: List[Chunk]) -> List[Chunk]:
        for chunk in chunks:
            chunk.embedding = get_embedding(chunk.text, model=self.model_name)
        return chunks
