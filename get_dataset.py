from PyPDF2 import PdfReader
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter

import os

# Read pdf file then maek chunks
def make_chunks(path='./data/case_study.pdf'):
    text = ""
    
    # Read pdf
    reader = PdfReader(path)
    # For each page, extract text and split it
    for page in reader.pages:
        text += page.extract_text()


    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )

    text_chunk = text_splitter.split_text(text)
    return text_chunk

# Create or load FAISS DB
def get_vector_store(texts: list) -> FAISS:
    # Use OpenAI word Embeddings
    embeddings = OpenAIEmbeddings()
    # If not exist
    if not os.path.exists("./db"):
        # Create DB
        print("Creating...")
        vectorstore = FAISS.from_texts(texts, embeddings)
        vectorstore.save_local("./db")
    else:
        # Load
        print("Loading...")
        vectorstore = FAISS.load_local("./db", embeddings)

    return vectorstore