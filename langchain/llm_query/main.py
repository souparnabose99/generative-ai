from langchain.llms import OpenAI
OPENAI_API_KEY = "xxx"


if __name__ == "__main__":
    llm = OpenAI(openai_api_key=OPENAI_API_KEY)
    res = llm("Share useful information about our solar system")
    print(res)