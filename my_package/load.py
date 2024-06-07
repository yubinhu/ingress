# my_package/load.py
from typing import List
import pandas as pd
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
