import os
from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv

load_dotenv()

model = "gpt-4o-mini"
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

# Plot a chart of NVIDIA and TESLA stock price change.
#
# --------------------------------------------------------------------------------
# Assistant (to User):
#
# To plot a chart of NVIDIA and TESLA stock price changes, I will use the `yfinance` library to fetch the stock price data for NVIDIA (NVDA) and TESLA (TSLA). After fetching the data, I'll use the `matplotlib` library to plot the stock prices over a specified time period.
#
# Here’s a step-by-step plan:
#
# 1. Install the required libraries (`yfinance` and `matplotlib`).
# 2. Fetch the historical stock data for NVIDIA and TESLA.
# 3. Plot the stock price changes for both companies on the same chart.
#
# First, I will provide the Python code to install the necessary libraries and then fetch the data.
#
# ```python
# # filename: fetch_stocks.py
# import yfinance as yf
# import matplotlib.pyplot as plt
#
# # Fetch historical data
# nvidia = yf.Ticker("NVDA")
# tesla = yf.Ticker("TSLA")
#
# # Get the historical prices
# nvidia_data = nvidia.history(period="1y")  # Last year
# tesla_data = tesla.history(period="1y")
#
# # Plotting the stock prices
# plt.figure(figsize=(14, 7))
# plt.plot(nvidia_data.index, nvidia_data['Close'], label='NVIDIA (NVDA)', color='blue')
# plt.plot(tesla_data.index, tesla_data['Close'], label='TESLA (TSLA)', color='orange')
#
# plt.title('NVIDIA and TESLA Stock Price Change Over the Last Year')
# plt.xlabel('Date')
# plt.ylabel('Stock Price (USD)')
# plt.legend()
# plt.grid()
# plt.show()
# ```
#
# Please save this code to a file named `fetch_stocks.py` and run it to plot the stock price change chart.
#
# --------------------------------------------------------------------------------
# Replying as user. Provide feedback to Assistant. Press enter to skip and use auto-reply, or type 'exit' to end the conversation:
