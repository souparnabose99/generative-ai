from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
from linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parser import summary_parser


def summarize_profile(name: str) -> str:
    linkedin_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_url, mock=True)

    summary_template = """
        given the LinkedIn information {information} about a person, I want you to create:
        1. A short summary
        2. 2 interesting facts about them
        
        \n{format_instructions}
        """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={"format_instructions": summary_parser.get_format_instructions()})
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = summary_prompt_template | llm | summary_parser
    # linked_data = scrape_linkedin_profile("", True)
    res = chain.invoke(input={"information": linkedin_data})
    print("LLM Output :\n", res)


if __name__ == "__main__":
    load_dotenv()
    print("---Profile Summarizer---\n")
    summarize_profile(name="Provide your name")

# Output:
# ---Profile Summarizer---
#
# LLM Output :
#  content='1. Short Summary:\nEden Marco is a Customer Engineer at Google, based in Tel Aviv, Israel. With a background in backend development and a successful career as a best-selling Udemy instructor, Eden brings a wealth of technical expertise and teaching experience to his role at Google.\n\n2. Interesting Facts:\n- Eden has produced and published two best-selling courses on the Udemy platform, with over 9,000 enrolled students, 800+ ratings, and a solid 4.7-star rating.\n- Prior to his current role, Eden served as a Captain in the Israel Defense Forces, showcasing his leadership skills and dedication to serving his country.'
