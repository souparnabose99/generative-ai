import os
import warnings
from colorama import Fore
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
warnings.filterwarnings("ignore")

# LOAD ENV VARIABLES
load_dotenv()

# Load the model
model = ChatOpenAI()

# Load the documents = https://python.langchain.com/docs/get_started/introduction
loader = WebBaseLoader("https://python.langchain.com/docs/get_started/introduction")
documents = loader.load()

# prompt templates
template = "you are senior developer who answers {question}  based on your knowledge based on {context}"
prompt = PromptTemplate(template=template, input_variables=["question", "context"])

