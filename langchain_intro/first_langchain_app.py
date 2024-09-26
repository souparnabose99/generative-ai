from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

information = """
Elon Reeve Musk FRS is a businessman and investor known for his key roles in the space company SpaceX and the automotive company Tesla, Inc.
"""

if __name__ == "__main__":
    print("First LangChain App")
    load_dotenv()

    summary_template = """
    given the information {information} about a person from I want to create:
    1. a short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables="information", template=summary_template)
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    # temperature decides how creative the language model is

    chain = summary_prompt_template | llm
    res = chain.invoke(input={"information": information})

    print(res)

# Output:
# content='1. Elon Musk is a renowned businessman and investor, best known for his involvement in SpaceX and Tesla, Inc.\n\n2. Two interesting facts about Elon Musk are:\n   - He is also the founder of The Boring Company, which aims to reduce traffic congestion through underground tunnel systems.\n   - Musk has expressed interest in colonizing Mars and has plans to establish a human settlement on the planet.'
