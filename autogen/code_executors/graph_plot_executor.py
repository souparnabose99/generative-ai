import os
from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv

load_dotenv()

model = "gpt-3.5-turbo"
llm_config = {
    "model": model,
    "api_key": os.environ.get("OPENAI_API_KEY"),
}

assistant = AssistantAgent(
    name="Assistant",
    llm_config=llm_config,
)

user_proxy = UserProxyAgent(
    name="User",
    human_input_mode="ALWAYS",
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False,  # change to True if you want to use docker
    },
)

user_proxy.initiate_chat(
    assistant, message="Plot a chart of NVIDIA and TESLA stock price change."
)

# Output:

# User (to Assistant):
#
# Plot a chart of NVIDIA and TESLA stock price change.
#
# --------------------------------------------------------------------------------
# Assistant (to user):
#
# To plot a chart of NVIDIA and TESLA stock price change, we first need to collect the historical stock price data for both companies. We can retrieve this data using a financial data API like Alpha Vantage. Once we have the data, we can use a Python library like Matplotlib to create the chart.
#
# Here is the plan:
# 1. Use Alpha Vantage API to get historical stock price data for NVIDIA and TESLA.
# 2. Process the data to extract the stock price information we need.
# 3. Use Matplotlib to create a chart displaying the stock price change over time for both companies.
#
# Let's start by retrieving the historical stock price data for NVIDIA and TESLA using the Alpha Vantage API.
#
# --------------------------------------------------------------------------------
# Replying as user. Provide feedback to Assistant. Press enter to skip and use auto-reply, or type 'exit' to end the conversation:
