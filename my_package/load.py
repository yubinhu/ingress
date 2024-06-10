# my_package/load.py
from typing import List
import pandas as pd
import json
import os
from .data_models import Document

class BaseLoader:
    def load(self) -> List[Document]:
        raise NotImplementedError

class FootballNewsLoader(BaseLoader):
    def __init__(self, directory_path: str):
        self.directory_path = directory_path

    def load(self) -> List[Document]:
        documents = []
        for filename in os.listdir(self.directory_path):
            if filename.endswith(".csv"):
                file_path = os.path.join(self.directory_path, filename)
                df = pd.read_csv(file_path)
                for i, row in df.iterrows():
                    document = Document(
                        id=str(i),
                        dataset='football',
                        title=str(row['title']) if pd.notna(row['title']) else "",
                        text=str(row['content']) if pd.notna(row['content']) else ""
                    )
                    documents.append(document)
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
