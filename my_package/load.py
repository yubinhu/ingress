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
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self) -> List[Document]:
        df = pd.read_csv(self.file_path)
        documents = [
            Document(id=str(i), dataset='football', title=row['title'], text=row['content'])
            for i, row in df.iterrows()
        ]
        return documents

class FinancialNewsLoader(BaseLoader):
    def __init__(self, directory_path: str):
        self.directory_path = directory_path

    def load(self) -> List[Document]:
        documents = []
        for filename in os.listdir(self.directory_path):
            if filename.endswith(".json"):
                file_path = os.path.join(self.directory_path, filename)
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
