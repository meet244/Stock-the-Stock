import yfinance as yf
import matplotlib.pyplot as plt

# Fetching historical data for a stock (e.g., Apple Inc. - AAPL)
stock = yf.Ticker("^BSESN")
data = stock.history(start="2000-01-01", end="2023-12-31")  # Adjust the dates as needed

max_value = 0
differences = []

for index in range(len(data)):
    close_value = data['Close'][index]
    
    if close_value > max_value:
        max_value = close_value
    
    difference = close_value - max_value
    differences.append(difference)

# Plotting
plt.figure(figsize=(10, 6))

for i in range(len(differences)):
    if differences[i] < 0:
        plt.plot(data.index[i], data['Close'][i], 'ro')  # 'ro' for red color
    elif differences[i] == 0:
        plt.plot(data.index[i], data['Close'][i], 'yo')  # 'yo' for yellow color
    else:
        plt.plot(data.index[i], data['Close'][i], 'go')  # 'go' for green color

plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('Stock Price Analysis')
plt.show()
