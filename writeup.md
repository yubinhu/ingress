# Design Writeup
## Design Overview
1.	Loading Data
- Objective: Efficiently load data from various formats (e.g., CSV, JSON) and convert them into a standard Document format.
- Classes:
    - BaseLoader: An abstract base class that defines the load method.
    - FootballNewsLoader: Inherits from BaseLoader and loads football news articles dataset from CSV files.
    - FinancialNewsLoader: Inherits from BaseLoader and loads financial news articles dataset from JSON files.
- Key Decisions:
    - Since we have a lot of data, we select to discard any document with defective data instead of trying to fix them.
    - The separation of the data model from functional components allows for easy additions of new loaders and modifications of data models.
2.	Chunking Documents
    - Objective: Break down large documents into smaller chunks for efficient processing.
    - Classes:
        - DocumentChunker: Responsible for chunking documents into smaller components.
    - Key Decisions:
        - The chunking strategy is to cut the document text into fixed-size chunks (e.g., 200 characters). This is probably sufficient for simple use cases. 
        - This design can be extended to support more complex chunking strategies, such as sentence-based or paragraph-based chunking. 
3.	Embedding Chunks
    - Objective: Generate embeddings for each chunk to facilitate downstream tasks such as search and retrieval.
    - Classes:
        - Embedder: Handles the generation of embeddings for each chunk using a specified model.
    - Key Decisions:
        - Uses an external service (e.g., OpenAI's embedding model) to generate embeddings. This can be easily replaced with other embedding models.
## Interaction Between Classes
1.	Loading Phase: The appropriate loader (e.g., FootballNewsLoader, FinancialNewsLoader) is instantiated and used to load raw data into Document objects.
2.	Chunking Phase: The DocumentChunker processes each Document, creating a list of Chunk objects.
3.	Embedding Phase: The Embedder takes the list of Chunk objects and generates embeddings for each chunk.
## Adding New Datasets
To add a new dataset, a developer would:
1.	Create a new loader class inheriting from BaseLoader.
2.	Implement the load method to read and convert raw data into Document objects.
3.	Integrate the new loader into the pipeline by instantiating it and calling its load method.
## Testing Strategy
1.	Unit Tests:
    - Unit tests can be easily written up for chunking and embedding components to make sure they don't break on existing datasets.
2.	Integration Tests:
    - There is an example of an integration test in test.ipynb that tests the entire pipeline on both datasets.
3.	Performance Tests:
    - Measure the pipeline's performance with large datasets and distributed systems to ensure it meets scalability requirements.
