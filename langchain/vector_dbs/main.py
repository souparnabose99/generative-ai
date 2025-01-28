import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_pinecone import PineconeVectorStore
from langchain import hub
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain


def perform_rag_steps():
    load_dotenv()
    embeddings = OpenAIEmbeddings()
    llm = ChatOpenAI()

    query = "What is Pinecone in Machine Learning?"
    chain = PromptTemplate.from_template(template=query) | llm
    result = chain.invoke(input={})

    print(result.content)

    vector_store = PineconeVectorStore(
        index_name=os.environ["INDEX_NAME"], embedding=embeddings
    )

    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")


if __name__ == "__main__":
    perform_rag_steps()


# Pinecone is a cloud-based vector database that is optimized for fast similarity search. It is designed specifically for machine learning applications that require high-performance search capabilities, such as recommendation systems, image search, and natural language processing. Pinecone allows users to store and query high-dimensional vectors efficiently, making it ideal for tasks that involve finding similar items in large datasets. It provides a simple API for adding, searching, and retrieving vectors, making it easy to integrate into machine learning pipelines.
