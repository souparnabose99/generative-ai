import yfinance as yf
import matplotlib.pyplot as plt

# Download historical stock data for Microsoft and Amazon
msft = yf.download('MSFT', start='2020-01-01', end='2023-10-01')
amzn = yf.download('AMZN', start='2020-01-01', end='2023-10-01')

# Plotting the closing prices for both stocks
plt.figure(figsize=(14, 7))
plt.plot(msft['Close'], label='Microsoft (MSFT)', color='blue')
plt.plot(amzn['Close'], label='Amazon (AMZN)', color='orange')

# Adding titles and labels
plt.title('Stock Price Change: Microsoft vs Amazon')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid()

# Show the plot
plt.show()