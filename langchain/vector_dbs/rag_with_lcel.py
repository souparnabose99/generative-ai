import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_pinecone import PineconeVectorStore
from langchain_core.runnables import RunnablePassthrough


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def perform_rag_steps():
    load_dotenv()
    embeddings = OpenAIEmbeddings()
    llm = ChatOpenAI()

    # Non RAG LLM invocation
    query = "What is Vector Database in Machine Learning?"
    chain = PromptTemplate.from_template(template=query) | llm
    result = chain.invoke(input={})
    print(result.content)

    vector_store = PineconeVectorStore(
        index_name=os.environ["INDEX_NAME"], embedding=embeddings
    )

    template = """Use the following pieces of context to answer the question at the end.
    If you don't know the answer, just say that you don't know, dont try to make up an answer.
    Use three sentences maximum and keep the answer as concise as possible.
    Always say 'Thanks for your query" at the end of the answer.
    
    {context}
    
    Question: {question}
    
    Answer: """

    custom_rag_prompt = PromptTemplate.from_template(template)

    rag_chain = (
        {"context": vector_store.as_retriever() | format_docs, "question": RunnablePassthrough()}
        | custom_rag_prompt
        | llm
    )

    result = rag_chain.invoke(query)
    print(result)


if __name__ == "__main__":
    perform_rag_steps()


# Pinecone is a cloud-based vector database that is optimized for fast similarity search. It is designed specifically for machine learning applications that require high-performance search capabilities, such as recommendation systems, image search, and natural language processing. Pinecone allows users to store and query high-dimensional vectors efficiently, making it ideal for tasks that involve finding similar items in large datasets. It provides a simple API for adding, searching, and retrieving vectors, making it easy to integrate into machine learning pipelines.
