from PyPDF2 import PdfReader
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter

import os

# Read pdf file then maek chunks
def make_chunks(files):
    text = ""
    
    # Read pdf
    for pdf in files:
        reader = PdfReader(pdf)
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
    vectorstore = FAISS.from_texts(texts, OpenAIEmbeddings())

    return vectorstore