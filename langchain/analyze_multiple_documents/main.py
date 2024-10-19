import os
from pydantic import BaseModel, Field
from langchain.chat_models import ChatOpenAI
from langchain.agents import Tool, initialize_agent, AgentType
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
os.environ['OPENAI_API_KEY'] = ""


if __name__ == "__main__":
    class DocumentInput(BaseModel):
        question: str = Field()


    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")

    tools = []
    files = [
        {
            "name": "alphabet-earnings",
            "path": "https://abc.xyz/investor/static/pdf/2023Q1_alphabet_earnings_release.pdf",
        },
        {
            "name": "Cisco-earnings",
            "path": "https://d18rn0p25nwr6d.cloudfront.net/CIK-0000858877/5b3c172d-f7a3-4ecb-b141-03ff7af7e068.pdf",
        },
        {
            "name": "IBM-earnings",
            "path": "https://www.ibm.com/investor/att/pdf/IBM_Annual_Report_2022.pdf",
        },
    ]

    for file in files:
        loader = PyPDFLoader(file["path"])
        pages = loader.load_and_split()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        docs = text_splitter.split_documents(pages)
        embeddings = OpenAIEmbeddings()
        retriever = FAISS.from_documents(docs, embeddings).as_retriever()
        # Wrap retrievers in a Tool
        tools.append(
            Tool(
                args_schema=DocumentInput,
                name=file["name"],
                func=RetrievalQA.from_chain_type(llm=llm, retriever=retriever),
            )
        )

    llm = ChatOpenAI(
        temperature=0,
        model="gpt-3.5-turbo-0613",
    )
    agent = initialize_agent(
        agent=AgentType.OPENAI_FUNCTIONS,
        tools=tools,
        llm=llm,
        verbose=True,
    )

    response = agent({"input": "Based on these SEC filing documents, identify \
            which of these three companies - Alphabet, IBM, and Cisco \
            has the greatest short-term debt levels and which has the \
            highest research and development costs."})

    print(response)

# Output ‘output’: ‘Based on the SEC filing documents:\n\n- The company with the greatest short-term debt levels is
# IBM, with a short-term debt level of $4,760 million.\n- The company with the highest research and development costs
# is Alphabet, with research and development costs of $11,468 million.’

