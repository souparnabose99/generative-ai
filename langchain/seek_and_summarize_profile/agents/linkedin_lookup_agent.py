import os
from dotenv import load_dotenv
from langchain import hub
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

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 Linkedin profile page",
            func="?",
            description="useful for when you need to get the Linkedin Page Url"
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linkedin_profile_url = result["output"]
    return linkedin_profile_url

