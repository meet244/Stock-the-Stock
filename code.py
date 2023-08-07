# Import necessary libraries
from datetime import datetime, timedelta
import yfinance as yf

# Function to calculate the average of a list of numbers
def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

# Define the BSE Sensex ticker
bse_sensex = yf.Ticker("^BSESN")

# Get the current date and time
current_date = datetime.now()

# Define a time period of 25 years ago
years_ago = timedelta(days=365 * 25)
new_date = current_date - years_ago

# Format the new date as a string
formatted_date = new_date.strftime('%Y-%m-%d')

# Print the start date
# print("Start Date:", formatted_date)

# Get historical data for BSE Sensex from the start date
historical_data = bse_sensex.history(start=formatted_date)

# Define a percentage change threshold
percent = 15  # Change this according to your need to improve accuracy

# Initialize variables for tracking peak, current close, buying status, and indicator
peak = 1
current_close = 0
is_buying = 0
indicator = 0

# Find the highest close value in historical data
highest_close = historical_data['Close'].max()

# Find the date corresponding to the highest close
highest_close_date = historical_data[historical_data['Close'] == highest_close].index[0]

# Trim historical data to start from the highest close date
trimmed_data = historical_data.loc[highest_close_date:]

# Loop through the trimmed data to analyze and make decisions
for date_str, row in trimmed_data.iterrows():
    # Convert date string to a datetime object
    date_obj = datetime.strptime(date_str.strftime("%Y-%m-%d"), "%Y-%m-%d")
    
    # Get the current close value
    current_close = int(row["Close"])
    
    # Calculate the percentage change from the peak
    change_percent = round(((current_close - peak) / peak) * 100, 2)
    
    # Determine the indicator value based on the percentage change
    indicator = 0 if change_percent <= -percent else 1 if change_percent >= percent else round(
        (change_percent - (-percent)) / (percent - (-percent)), 2)
    
    # Print date, close value, percentage change, and indicator
    # print(f"{date_obj.date()}\t{current_close}\t{change_percent}\t{indicator}")
    
    # Check conditions for buying and selling
    if (change_percent <= -percent and is_buying == 0):
        is_buying = 1
        # print("Buying")
        buy_price = current_close
    elif (change_percent >= percent and is_buying == 1):
        is_buying = 0
        # print("Selling")
    
    # Update peak value if a new peak is found
    if (peak < current_close and is_buying == 0):
        peak = current_close
        # print(f"Peak = {peak}")

# Print final results
print("X Peak:", peak)
print("Current Close:", current_close)
print("Final Indicator:", indicator) # Here 0 = sell and 1 = buy else hold - based on the percentage

# Determine the final decision based on the indicator value
if indicator == 0:
    print("Final Decision: Sell")
elif indicator == 1:
    print("Final Decision: Buy")
else:
    print("Final Decision: Hold")
