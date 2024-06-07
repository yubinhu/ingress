# my_package/data_models.py
from typing import List

class Document:
    def __init__(self, id: str, dataset: str, title: str, text: str):
        self.id = id
        self.dataset = dataset
        self.title = title
        self.text = text
    
    def __repr__(self):
        return f"Document(id={self.id}, dataset={self.dataset}, title={self.title[:20]}..., text={self.text[:20]}...)"

class Chunk:
    def __init__(self, id: str, doc_id: str, text: str):
        self.id = id
        self.doc_id = doc_id
        self.text = text
        self.embedding = []

    def __repr__(self):
        return f"Chunk(id={self.id}, doc_id={self.doc_id}, text={self.text[:20]}..., embedding={self.embedding[:5]})"
