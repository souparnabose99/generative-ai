import yfinance as yf
import matplotlib.pyplot as plt

# Download historical stock data for Google and Apple
googl = yf.download('GOOGL', start='2020-01-01', end='2023-10-01')
aapl = yf.download('AAPL', start='2020-01-01', end='2023-10-01')

# Plotting the closing prices for both stocks
plt.figure(figsize=(14, 7))
plt.plot(googl['Close'], label='Google (GOOGL)', color='green')
plt.plot(aapl['Close'], label='Apple (AAPL)', color='red')

# Adding titles and labels
plt.title('Stock Price Change: Google vs Apple')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid()

# Show the plot
plt.show()