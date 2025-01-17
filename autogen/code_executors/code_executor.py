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
    assistant, message="Plot a chart of MICROSOFT and AMAZON stock price change."
)

# Output:

# E:\Coding-Mastery\AutoGen\projects\autogen\Scripts\python.exe E:\Coding-Mastery\AutoGen\projects\code_executors\code_executor.py
# E:\Coding-Mastery\AutoGen\projects\autogen\Lib\site-packages\flaml\__init__.py:20: UserWarning: flaml.automl is not available. Please install flaml[automl] to enable AutoML functionalities.
#   warnings.warn("flaml.automl is not available. Please install flaml[automl] to enable AutoML functionalities.")
# User (to Assistant):
#
# Plot a chart of MICROSOFT and AMAZON stock price change.
#
# --------------------------------------------------------------------------------
# Assistant (to User):
#
# To plot the stock price change for Microsoft and Amazon, we will follow these steps:
#
# 1. **Collect historical stock price data for Microsoft (MSFT) and Amazon (AMZN)**.
# 2. **Use libraries such as `pandas` and `matplotlib` to process and visualize the data**.
#
# Here’s the plan with the necessary Python code:
#
# - We'll use the `yfinance` library to download the stock data for both companies.
# - We'll plot the closing prices over time.
#
# Let's get started by creating a script that collects and plots this data.
#
# ```python
# # filename: plot_stocks.py
# import yfinance as yf
# import matplotlib.pyplot as plt
#
# # Download historical stock data for Microsoft and Amazon
# msft = yf.download('MSFT', start='2020-01-01', end='2023-10-01')
# amzn = yf.download('AMZN', start='2020-01-01', end='2023-10-01')
#
# # Plotting the closing prices for both stocks
# plt.figure(figsize=(14, 7))
# plt.plot(msft['Close'], label='Microsoft (MSFT)', color='blue')
# plt.plot(amzn['Close'], label='Amazon (AMZN)', color='orange')
#
# # Adding titles and labels
# plt.title('Stock Price Change: Microsoft vs Amazon')
# plt.xlabel('Date')
# plt.ylabel('Stock Price (USD)')
# plt.legend()
# plt.grid()
#
# # Show the plot
# plt.show()
# ```
#
# Please save the above code in a file named `plot_stocks.py` and then execute it. After execution, please confirm whether the plot displays correctly.
#
# TERMINATE
#
# --------------------------------------------------------------------------------
# Replying as User. Provide feedback to Assistant. Press enter to skip and use auto-reply, or type 'exit' to end the conversation: How about Google & Apple
# User (to Assistant):
#
# How about Google & Apple
#
# --------------------------------------------------------------------------------
# Assistant (to User):
#
# We can follow the same approach to plot the stock price change for Google (Alphabet Inc., ticker symbol GOOGL) and Apple (AAPL).
#
# Here’s the updated Python code to download and plot the stock price data for both companies:
#
# ```python
# # filename: plot_google_apple_stocks.py
# import yfinance as yf
# import matplotlib.pyplot as plt
#
# # Download historical stock data for Google and Apple
# googl = yf.download('GOOGL', start='2020-01-01', end='2023-10-01')
# aapl = yf.download('AAPL', start='2020-01-01', end='2023-10-01')
#
# # Plotting the closing prices for both stocks
# plt.figure(figsize=(14, 7))
# plt.plot(googl['Close'], label='Google (GOOGL)', color='green')
# plt.plot(aapl['Close'], label='Apple (AAPL)', color='red')
#
# # Adding titles and labels
# plt.title('Stock Price Change: Google vs Apple')
# plt.xlabel('Date')
# plt.ylabel('Stock Price (USD)')
# plt.legend()
# plt.grid()
#
# # Show the plot
# plt.show()
# ```
#
# Please save the above code in a file named `plot_google_apple_stocks.py` and then execute it. After execution, please confirm whether the plot displays correctly.
#
# TERMINATE
#
# --------------------------------------------------------------------------------
# Replying as User. Provide feedback to Assistant. Press enter to skip and use auto-reply, or type 'exit' to end the conversation: exit
#
# Process finished with exit code 0