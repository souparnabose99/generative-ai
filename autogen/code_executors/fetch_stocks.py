import yfinance as yf
import matplotlib.pyplot as plt

# Fetch historical data
nvidia = yf.Ticker("NVDA")
tesla = yf.Ticker("TSLA")

# Get the historical prices
nvidia_data = nvidia.history(period="1y")  # Last year
tesla_data = tesla.history(period="1y")

# Plotting the stock prices
plt.figure(figsize=(14, 7))
plt.plot(nvidia_data.index, nvidia_data['Close'], label='NVIDIA (NVDA)', color='blue')
plt.plot(tesla_data.index, tesla_data['Close'], label='TESLA (TSLA)', color='orange')

plt.title('NVIDIA and TESLA Stock Price Change Over the Last Year')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid()
plt.show()
