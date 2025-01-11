import os
from autogen import AssistantAgent, UserProxyAgent, ConversableAgent
from dotenv import load_dotenv

load_dotenv()

model = "gpt-4o-mini"

llm_config = {
    "model": model,
    "api_key": os.environ.get("OPENAI_API_KEY")
}

