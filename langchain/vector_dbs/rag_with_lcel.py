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

    query = "What is Vector Database in Machine Learning?"
    #query = "What is Pinecone in Machine Learning?"
    chain = PromptTemplate.from_template(template=query) | llm
    result = chain.invoke(input={})

    print(result.content)

    vector_store = PineconeVectorStore(
        index_name=os.environ["INDEX_NAME"], embedding=embeddings
    )

    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    combine_docs_chain = create_stuff_documents_chain(llm, retrieval_qa_chat_prompt)
    retrieval_chain = create_retrieval_chain(
        retriever=vector_store.as_retriever(), combine_docs_chain=combine_docs_chain
    )

    result = retrieval_chain.invoke(input={"input": query})
    print(result)

    template = """Use the following pieces of context to answer the question at the end.
    If you don't know the answer, just say that you don't know, dont try to make up an answer.
    Use three sentences maximum and keep the answer as concise as possible.
    Always say 'Thanks for your query" at the end of the answer.
    
    {context}
    
    Question: {question}
    
    Answer: """

    custom_rag_prompt = PromptTemplate.from_template(template)


if __name__ == "__main__":
    perform_rag_steps()


# Pinecone is a cloud-based vector database that is optimized for fast similarity search. It is designed specifically for machine learning applications that require high-performance search capabilities, such as recommendation systems, image search, and natural language processing. Pinecone allows users to store and query high-dimensional vectors efficiently, making it ideal for tasks that involve finding similar items in large datasets. It provides a simple API for adding, searching, and retrieving vectors, making it easy to integrate into machine learning pipelines.
