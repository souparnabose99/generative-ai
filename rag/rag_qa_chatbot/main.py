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
    pass


def load_embeddings(documents):
    """Create a vector store from a set of documents."""
    pass


def generate_response(retriever, query):
    """Generate a response using the retriever and the query."""
    # Create a prompt template using a template from the config module and input variables
    # representing the context and question.
    # create the prompt
    pass


def query(query_str):
    """Query the model and return the response."""
    pass


def start():
    pass


def ask():
    pass


if __name__ == "__main__":
    start()
