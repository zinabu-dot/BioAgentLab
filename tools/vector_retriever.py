# tools/vector_retriever.py

import os
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings


class VectorRetriever:
    """
    Loads biomedical documents and retrieves relevant context using vector similarity.
    """

    def __init__(self, docs_path="data/literature"):
        self.docs_path = docs_path
        self.vectorstore = self._load_or_create_index()

    def _load_or_create_index(self):
        print("[VectorRetriever] Loading documents...")
        docs = []

        # Load all .txt files in the data directory
        for filename in os.listdir(self.docs_path):
            if filename.endswith(".txt"):
                loader = TextLoader(os.path.join(self.docs_path, filename))
                docs.extend(loader.load())

        print(f"[VectorRetriever] Loaded {len(docs)} documents.")

        # Split documents into chunks
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        split_docs = splitter.split_documents(docs)

        print(f"[VectorRetriever] Split into {len(split_docs)} chunks.")

        # Create FAISS index
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        return FAISS.from_documents(split_docs, embeddings)

    def retrieve(self, query: str) -> str:
        """
        Retrieve top documents most similar to the input query.
        """
        print(f"[VectorRetriever] Retrieving for query: {query}")
        docs = self.vectorstore.similarity_search(query, k=3)
        return "\n\n".join([f"📄 {doc.page_content}" for doc in docs])
