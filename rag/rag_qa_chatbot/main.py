import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.text_splitter import (
    CharacterTextSplitter,
)
from langchain.prompts.chat import (
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain_community.vectorstores import Chroma
from colorama import Fore
import warnings

warnings.filterwarnings("ignore")

load_dotenv()

template: str = """/
    You are a customer support specialist /
    question: {question}. You assist users with general inquiries based on {context} /
    and  technical issues. /
    """
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_message_prompt = HumanMessagePromptTemplate.from_template(
    input_variables=["question", "context"],
    template="{question}",
)
chat_prompt_template = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt]
)

model = ChatOpenAI()


def load_documents():
    """Load a file from path, split it into chunks, embed each chunk and load it into the vector store."""
    loader = TextLoader("./user-manual.txt")
    raw_text = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    return text_splitter.split_documents(raw_text)


def load_embeddings(documents):
    """Create a vector store from a set of documents."""
    embeddings = OpenAIEmbeddings()
    db = Chroma.from_documents(documents, embeddings)
    return db.as_retriever()


def generate_response(retriever, query):
    """Generate a response using the retriever and the query."""
    chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | chat_prompt_template
            | model
            | StrOutputParser()
    )
    return chain.invoke(query)


def query(query_str):
    """Query the model and return the response."""
    documents = load_documents()
    retriever = load_embeddings(documents)
    response = generate_response(retriever, query_str)
    return response


def start():
    pass


def ask():
    pass


if __name__ == "__main__":
    start()
