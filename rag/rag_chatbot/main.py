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

# RETRIEVER - Load embeddings and create a vector store
embeddings = OpenAIEmbeddings()
vector_store = FAISS.from_documents(documents, embeddings)


# GENERATE - Define the function to generate the response
def generate(query):
    chain_type_kwargs = {"prompt": prompt}
    chain = RetrievalQA.from_chain_type(llm=model, chain_type="stuff", retriever=vector_store.as_retriever(search_kwargs={"k": 1}), chain_type_kwargs=chain_type_kwargs,)
    response = chain.run(query)
    return response


def start():
    print("OPENAI API KEY", os.getenv("OPENAI_API_KEY"))
    print("documents", documents)
    instructions = (
        "Type your question and press ENTER. Type 'x' to go back to the MAIN menu.\n"
    )
    print(Fore.RED + "\n\x1B[3m" + instructions + "\x1B[0m" + Fore.RESET)

    print("MENU")
    print("====")
    print("[1]- Ask a question")
    print("[2]- Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        ask()
    elif choice == "2":
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice")
        start()


def ask():
    while True:
        user_input = input("Q: ")
        # Exit
        if user_input == "x":
            start()
        else:
            response = generate(user_input)

            print(Fore.RED + f"A: " + response + Fore.RESET)
            print(Fore.WHITE + "\n-------------------------------------------------")


if __name__ == "__main__":
    start()

# MENU
# ====
# [1]- Ask a question
# [2]- Exit
# Enter your choice: 1
# Q: what is langchain?
# A: LangChain is a framework for developing applications powered by large language models (LLMs). It simplifies every stage of the LLM application lifecycle, including development,
# productionization, and deployment. LangChain implements a standard interface for large language models and integrates with various providers. It consists of multiple open-source li
# braries such as langchain-core, integration packages, langchain, langchain-community, and langgraph. These libraries provide abstractions for chat models, agents, retrieval strateg
# ies, and orchestration frameworks for building production-ready applications with persistence and streaming capabilities. LangChain also offers tutorials, how-to guides, conceptual guides, integrations, and an API reference to help developers get started with building applications using the framework.
#
# -------------------------------------------------
# Q: