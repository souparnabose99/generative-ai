from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
from linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    load_dotenv()
    print("---Profile Summarizer---\n")

    summary_template = """
    given the LinkedIn information {information} about a person, I want you to create:
    1. A short summary
    2. 2 interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = summary_prompt_template | llm
    linked_data = scrape_linkedin_profile("", True)
    res = chain.invoke(input={"information": linked_data})
    print("LLM Output :\n", res)
