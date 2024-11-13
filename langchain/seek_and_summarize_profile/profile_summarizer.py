from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    print("Profile Summarizer")

    summary_template = """
    given the information {information} about a person, I want you to create:
    1. A short summary
    2. 2 interesting facts about them
    """

