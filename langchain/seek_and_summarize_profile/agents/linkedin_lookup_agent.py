import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)


load_dotenv()


def lookup(name: str) -> str:
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-4o-mini"
    )

    template = """
    given the full name of a person {name_of_a_person} I want you to get me a link to their LinkedIn profile page.
    Your answer should contain only a url
    """

    prompt_template = PromptTemplate(
        template=template,
        input_variables=["name_of_a_person"]
    )

    

    return "https://www.linked.com/in/eden-marco/"

