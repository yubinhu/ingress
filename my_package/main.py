# main.py
from my_package.load import FootballNewsLoader
from my_package.document_chunker import DocumentChunker
from my_package.embed import Embedder

def main():
    # Step 1: Load data
    loader = FootballNewsLoader(file_path='./data/football/allfootball.csv')
    documents = loader.load()

    # Step 2: Chunk documents
    chunker = DocumentChunker()
    all_chunks = []
    for document in documents:
        chunks = chunker.chunk(document)
        all_chunks.extend(chunks)

    # Step 3: Embed chunks
    embedder = Embedder()
    embedded_chunks = embedder.embed(all_chunks)

    # Further processing or saving embedded_chunks
    print(f"Processed {len(embedded_chunks)} chunks.")

if __name__ == '__main__':
    main()
 