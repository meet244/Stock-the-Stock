# Import necessary libraries
import yfinance as yf
from datetime import date
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the average of a list of numbers
def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

# Define the BSE Sensex ticker
# bse_sensex = yf.Ticker("TATAMOTORS.NS")
bse_sensex = yf.Ticker("^BSESN")

# Get historical data for BSE Sensex from the start date
st.title("Stock the Stock")

# Allow user to select start and end dates
st.markdown('## Select Start and End Dates')
st.caption("Please enter the start and end dates for the analysis.")
start_date = st.date_input("Start Date", value=date(1970, 1, 1))
end_date = st.date_input("End Date", value=date.today())

# Allow user to select stock/index
st.markdown('## Select Stock/Index')
st.caption("Please enter the stock/index you want to analyze.")
# yahoo finance link
st.markdown("Get Stock/Index codes from [Yahoo Finance](https://finance.yahoo.com/)")
# stock_options = ["^BSESN", "TATAMOTORS.NS", "RELIANCE.NS", "HDFCBANK.NS"] # Add more options as needed
selected_stock = st.text_input("", "^BSESN") # Allow user to enter text, default value is "^BSESN"

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)  # Create 7 columns

# Place buttons in the columns
with col1:
    if st.button("^BSEN") and selected_stock != "^BSESN":
        selected_stock = "^BSESN"
        

with col2:
    if st.button("AAPL"):
        selected_stock = "AAPL"

with col3:
    if st.button("GOOG"):
        selected_stock = "GOOG"

with col4:
    if st.button("^GSPC"):
        selected_stock = "^GSPC"

with col5:
    if st.button("NFLX"):
        selected_stock = "NFLX"

with col6:
    if st.button("META"):
        selected_stock = "META"

with col7:
    if st.button("AMZN"):
        selected_stock = "AMZN"

# Define a percentage change threshold
st.markdown('## Select the Percentage')
st.caption("The percentage change threshold is used to determine the market fall and rise. The higher the percentage, the more the market has to fall/rise to be considered a fall/rise.")
percent = st.slider("", 5, 40, 20, format="%d%%") # Allow user to select percentage from range 5-40

# Initialize the ticker
ticker = yf.Ticker(selected_stock)

# Get historical data for the selected stock/index
historical_data = ticker.history(start=start_date.strftime("%Y-%m-%d"), end=end_date.strftime("%Y-%m-%d"))

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

# Streamlit app
st.markdown(f'## {selected_stock} Historical Data')
st.caption("The historical data of the stock/index is plotted below.")

# convey what coloured points means
st.markdown('**Yellow points** represent the peaks.')
st.markdown('**Red points** represent the market falls.')
st.markdown('**Green points** represent the market rises.')

# Plotting
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(historical_data.index, historical_data['Close'], color=color)
for pt, point_color in [(peaks, 'yellow'), (fall_points, 'red'), (rise_points, 'green')]:
    if len(pt) > 0:
        dates, closes = zip(*pt)
        ax.scatter(dates,    closes, color=point_color)

ax.set_xlabel('Date')
ax.set_ylabel('Closing Price')
st.pyplot(fig)


st.markdown('## Buy-Hold-Sell Indicator')
st.caption("The indicator shows whether you should buy, hold or sell the stock/index based on the current status of the market. It will ask to sell when the market is high and ask to buy when the market is low. This strategy is taken from the famous Warren Buffett's quote.")
st.markdown("> **Be fearful when others are greedy and greedy when others are fearful.**")
# check current status
percentage_change = (historical_data['Close'].iloc[-1] - peaks[-1][1]) / peaks[-1][1] * 100
# Calculate the color gradient
colors = np.linspace(0, 1, 100)
color_map = plt.cm.RdYlGn(colors)

# Calculate the position of the pointer
if percentage_change >= 20:
    pointer_position = 1  # Max sell
    text_position = 0.95  # Position of the text "sell"
elif percentage_change <= -20:
    pointer_position = 0.00 # Max buy
    text_position = 0.05  # Position of the text "buy"
else:
    pointer_position = (percentage_change + 20) / 40  # Linear interpolation between max buy and max sell
    text_position = pointer_position  # Position of the text "hold"

# Plot the buy-hold-sell bar with gradient color and pointer
fig, ax = plt.subplots(figsize=(6, 0.5))
ax.imshow([color_map], aspect='auto', extent=(0, 1, 0, 1))
ax.axvline(x=pointer_position, color='black', linewidth=2, ymin=-0.2, ymax=1.2, clip_on=False)
ax.set_axis_off()

# Add text labels
ax.text(0.05, 0.5, 'Buy', transform=ax.transAxes, ha='left', va='center', color='white')
ax.text(0.5, 0.5, 'Hold', transform=ax.transAxes, ha='center', va='center')
ax.text(0.95, 0.5, 'Sell', transform=ax.transAxes, ha='right', va='center', color='white')

st.pyplot(fig)


# display how much market is currently down from the max
st.markdown('## Current Status')
st.write("**Current value:** ", round(historical_data['Close'].iloc[-1], 2))
st.write("**Peak:** ", round(point,2))
st.write("**Down from peak:** ", round((historical_data['Close'].iloc[-1] - point) / point * 100, 2), "%")

# line break
st.divider()

# display warning that we are not financial advisors
st.markdown('### Disclaimer')
st.warning("We are not financial advisors. This is just a tool to help you make better decisions. Please consult a financial advisor before making any investment decisions.")
