import os

import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
os.environ["OPENAI_API_KEY"] = "xxxx"

OPENAI_API_KEY = "xxxxx"

# Upload pdf files
st.header("Personal Doc Analyzer Chatbot")


with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload a pdf & ask your questions", type="pdf")

# Extract text
if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
        # st.write(text)


# Perform data chunking
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n"],
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    st.write(chunks)

# Creating Embeddings
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)


# Creating FAISS Vector store
vector_store = FAISS.from_texts(chunks, embeddings)

