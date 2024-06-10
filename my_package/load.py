# my_package/load.py
from typing import List
import pandas as pd
import json
import os
import hashlib
from .data_models import Document

class BaseLoader:
    def load(self) -> List[Document]:
        raise NotImplementedError

class FootballNewsLoader(BaseLoader):
    def __init__(self, directory_path: str):
        self.directory_path = directory_path

    def _hash_content(self, content: str) -> str:
        # Create a hash of the content using SHA-256
        return hashlib.sha256(content.encode('utf-8')).hexdigest()

    def load(self) -> List[Document]:
        documents = []
        for filename in os.listdir(self.directory_path):
            if not filename.endswith(".csv"):
                continue
            file_path = os.path.join(self.directory_path, filename)
            df = pd.read_csv(file_path)
            for _, row in df.iterrows():
                content = str(row['content']) if pd.notna(row['content']) else None
                if not content:
                    continue
                document_id = self._hash_content(content)
                title = str(row['title']) if pd.notna(row['title']) else ""
                documents.append(Document(id=document_id, dataset='football', title=title, text=content))
        return documents

class FinancialNewsLoader(BaseLoader):
    def __init__(self, directory_path: str):
        self.directory_path = directory_path

    def load(self) -> List[Document]:
        documents = []
        for root, _, files in os.walk(self.directory_path):
            for filename in files:
                if filename.endswith(".json"):
                    file_path = os.path.join(root, filename)
                    with open(file_path, 'r') as file:
                        data = json.load(file)
                        document = Document(
                            id=data['uuid'],
                            dataset='financial',
                            title=data['title'],
                            text=data['text']
                        )
                        documents.append(document)
        return documents
