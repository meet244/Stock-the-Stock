# Import necessary libraries
from datetime import datetime, timedelta
import yfinance as yf
# Import necessary libraries
import matplotlib.pyplot as plt

# Initialize lists to store x and y values for plotting
x_values = []
y_values = []

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

# Get historical data for BSE Sensex from the start date
historical_data = bse_sensex.history(start=formatted_date)


# Reverse the order of historical data
historical_data = historical_data.iloc[::-1]

# Define a percentage change threshold
percent = 17  # Change this according to your need to improve accuracy

# Initialize variables for tracking peak, current close, buying status, and indicator
high_peak = 0
fallen = False
# peak = 1
# current_close = 0
# is_buying = 0
# indicator = 0

# Find the highest close value in historical data
highest_close = historical_data['Close'].max()

# Loop through the historical data to analyze and make decisions
for date_str, row in historical_data.iterrows():
    # Convert date string to a datetime object
    date_obj = datetime.strptime(date_str.strftime("%Y-%m-%d"), "%Y-%m-%d")
    
    # Get the current close value
    current_close = int(row["Close"])

    x_values.append(date_obj)
    y_values.append(current_close)

    if(current_close > high_peak):
        high_peak = current_close
    else:
        # calculate the percentage change from the peak
        change_percent = round(((high_peak - current_close) / high_peak) * 100, 2)

        # check if the percentage change is greater than or equal to -percent
        if change_percent >= -(percent*2):
            print("sell here")
            fallen = True
            break

        if fallen:
            # compare the percentage change from the peak to the -(percentage)
            if change_percent >= -percent:
                print("buy here")
                fallen = False
                break



# Plot the data
plt.plot(x_values, y_values, color='blue')

# Plot the data where fallen is True in red color
fallen_x_values = [x_values[i] for i in range(len(x_values)) if fallen]
fallen_y_values = [y_values[i] for i in range(len(y_values)) if fallen]
plt.plot(fallen_x_values, fallen_y_values, color='red')

# Show the plot
plt.show()



    # Determine the indicator value based on the percentage change
    # indicator = 0 if change_percent <= -40 else 1 if change_percent >= 20 else round(
    #     (change_percent - (-40)) / (20 - (-40)), 2)
    
    # Print date, close value, percentage change, and indicator
    # print(f"{date_obj.date()}\t{current_close}\t{change_percent}\t{indicator}")
    
    # Check conditions for buying and selling
    # if (change_percent <= -40 and is_buying == 0):
    #     is_buying = 1
    #     # print("Buying")
    #     buy_price = current_close
    # elif (change_percent >= 20 and is_buying == 1):
    #     is_buying = 0
    #     # print("Selling")
    
    # # Update peak value if a new peak is found
    # if (peak is None or peak < current_close and is_buying == 0):
    #     peak = current_close
    #     print(f"Peak Date: {date_obj.date()}")

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
