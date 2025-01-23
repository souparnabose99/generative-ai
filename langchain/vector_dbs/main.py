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

    query = "What is LangSmith in Machine Learning?"
    chain = PromptTemplate.from_template(template=query) | llm
    result = chain.invoke(input={})

    print(result.content)

    vector_store = PineconeVectorStore(
        index_name=os.environ["INDEX_NAME"], embedding=embeddings
    )

    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")


if __name__ == "__main__":
    perform_rag_steps()


# LangSmith is a language model introduced by OpenAI that is specifically trained on a large amount of text data to understand and generate human-like text. It is based on the GPT-3 model and is capable of performing a wide range of natural language processing tasks, such as text generation, translation, summarization, and more. LangSmith has been used in various applications, including chatbots, content generation, and language understanding tasks.
