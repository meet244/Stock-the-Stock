import yfinance as yf
import matplotlib.pyplot as plt

# Fetch historical data for Sensex
sensex = yf.download('^BSESN', start='2018-01-01', end='2023-12-31')

# Initialize variables
highest_price = 0
lowest_dip = 0
dips = []
rises = []

for index, row in sensex.iterrows():
    current_price = row['Close']

    # Update highest price
    if current_price > highest_price:
        highest_price = current_price

    # Check for dip
    if highest_price * 0.8 >= current_price:
        dips.append((index, current_price))
        lowest_dip = current_price

    # Check for rise
    if lowest_dip * 1.4 <= current_price:
        rises.append((index, current_price))
        lowest_dip = 0

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(sensex.index, sensex['Close'], color='blue', label='Sensex')

dip_dates, dip_values = zip(*dips)
rise_dates, rise_values = zip(*rises)

plt.scatter(dip_dates, dip_values, color='red', label='Dips')
plt.scatter(rise_dates, rise_values, color='green', label='Rises')

plt.xlabel('Date')
plt.ylabel('Sensex')
plt.title('Sensex Stock Analysis')
plt.legend()
plt.show()
