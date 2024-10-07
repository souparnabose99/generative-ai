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


def generate_response(retriever, query_str):
    """Generate a response using the retriever and the query."""
    chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | chat_prompt_template
            | model
            | StrOutputParser()
    )
    return chain.invoke(query_str)


def query(query_str):
    """Query the model and return the response."""
    documents = load_documents()
    retriever = load_embeddings(documents)
    response = generate_response(retriever, query_str)
    return response


def start():
    instructions = (
        "Type your question and press ENTER. Type 'x' to go back to the MAIN menu.\n"
    )
    print(Fore.BLUE + "\n\x1B[3m" + instructions + "\x1B[0m" + Fore.RESET)

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

            response = query(user_input)

            print(Fore.BLUE + f"A: " + response + Fore.RESET)
            print(Fore.WHITE + "\n-------------------------------------------------")


if __name__ == "__main__":
    start()

# python main.py
#
# Type your question and press ENTER. Type 'x' to go back to the MAIN menu.
#
# MENU
# ====
# [1]- Ask a question
# [2]- Exit
# Enter your choice: 1
# Q: I am getting error code E3 while running the washing machine
# Number of requested results 4 is greater than number of elements in index 1, updating n_results = 1
# A: Error code E3 on the Washing Machine XYZ indicates a drum rotation problem. To troubleshoot this issue, please follow these steps:
#
# 1. Check the laundry load: Make sure that the laundry inside the drum is evenly distributed. An unbalanced load can cause the drum rotation problem. Try rearranging the laundry to ensure balanced distribution.
#
# 2. Restart the washing machine: Stop the current cycle and restart the machine. Sometimes, a simple restart can resolve the error code E3.
#
# 3. If the issue persists after checking the laundry load and restarting the machine, please contact our after-sales service for further assistance. You can reach them at the phone number provided in the user manual: +33 880 880 887.
#
# If you need any additional help or have further questions, feel free to contact our customer service team at serviceclient@machinelaverxyz.com or visit our website at www.machinelaverxyz.com. Thank you for choosing the Washing Machine XYZ.
#
# -------------------------------------------------
# Q: x
#
# Type your question and press ENTER. Type 'x' to go back to the MAIN menu.
#
# MENU
# ====
# [1]- Ask a question
# [2]- Exit
# Enter your choice: 2
# Goodbye!

