# my_package/document_chunker.py
from typing import List
from .data_models import Document, Chunk

class DocumentChunker:
    def chunk(self, document: Document) -> List[Chunk]:
        chunks = []
        chunk_size = 200  # Example chunk size
        text = document.text
        for i in range(0, len(text), chunk_size):
            chunk_text = text[i:i + chunk_size]
            chunk = Chunk(id=f"{document.id}_{i // chunk_size}", doc_id=document.id, text=chunk_text)
            chunks.append(chunk)
        return chunks
