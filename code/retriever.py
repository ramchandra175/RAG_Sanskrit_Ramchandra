from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os


class Retriever:
    def __init__(self):
        # 🔹 Get project root directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # 🔹 Absolute path to data file
        DATA_PATH = os.path.join(BASE_DIR, "data", "sanskrit_docs.txt")

        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
        )

        loader = TextLoader(DATA_PATH, encoding="utf-8")
        documents = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        docs = splitter.split_documents(documents)

        self.vectorstore = FAISS.from_documents(docs, self.embeddings)

    def get_context(self, query, k=3):
        docs = self.vectorstore.similarity_search(query, k=k)
        context = "\n".join(doc.page_content for doc in docs)
        return context
