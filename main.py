# Import necessary libraries
import yfinance as yf
from datetime import date
import matplotlib.pyplot as plt

# Function to calculate the average of a list of numbers
def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

# Define the BSE Sensex ticker
# bse_sensex = yf.Ticker("^BSESN")
bse_sensex = yf.Ticker("^GSPC")

# Get historical data for BSE Sensex from the start date
today = date.today().strftime("%Y-%m-%d")
historical_data = bse_sensex.history(start="1970-01-01", end=today)

# Define a percentage change threshold
percent = 20 # Change this according to your need to improve accuracy

# Initialize variables to track peaks and color plotting
peaks = []
fall_points = []
rise_points = []
color = 'grey'
point = 0
point_index = 0
fallen = False
returns = [] # list of returns
buy_point = 0

# Calculate peaks and market falls/rises
for index, row in historical_data.iterrows():
    # Access the data in each row using row['column_name']
    # Perform necessary operations on the data
    close = row['Close']
    if(not fallen and close>point):
        point=close
        point_index=index
    
    # check if the fall happens
    if(not fallen and close<=point*(1-percent/100)):
        fall_points.append((index,close))
        fallen=True
        buy_point=close
        # mark point on graph blue
        peaks.append((point_index,point))

    # check if the rise happens
    if(fallen and close>=point*(1+percent/100)):
        rise_points.append((index,close))
        fallen=False
        returns.append((close-buy_point)/buy_point)

# Set the style to dark mode
# plt.style.use('dark_background')

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(historical_data.index, historical_data['Close'], color=color)
for point, point_color in [(peaks, 'blue'), (fall_points, 'red'), (rise_points, 'green')]:
    if len(point) > 0:
        dates, closes = zip(*point)
        plt.scatter(dates, closes, color=point_color)

plt.title('BSE Sensex Historical Data')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.show()

print(f"{percent} Total returns: ", sum(returns)*100)
print(f"{percent} Average returns: ", calculate_average(returns)*100)
print(f"{percent} Number of trades: ", len(returns))