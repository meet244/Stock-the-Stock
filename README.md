## 📈 Stock indicator 📊

# ❝ Be Fearful when others are Greedy, and Greedy when others are Fearful. ❞
Based on this famous investment philosophy of [Warren Buffett](https://en.wikipedia.org/wiki/Warren_Buffett). This script utilizes historical stock market data to make buy, sell, or hold decisions for a given stock.  🚀📉

### Overview 📋
The provided Python script analyzes historical stock data of a chosen stock (BSE Sensex in this example) and makes decisions based on the percentage change from the peak value. The script aims to identify buying opportunities during periods of significant price drops and selling opportunities during periods of substantial price increases.

### How It Works 🛠️
1. Import the necessary libraries and define functions. 📚📝
2. Get historical data for the chosen stock from the last 25 years. 📅📊
3. Find the highest close value and trim the data to start from that date. 📈🔍
4. Analyze the data and make buy/sell decisions based on specified percentage thresholds. 📊📉
5. Print the final decision: Buy, Sell, or Hold. 📜🤝

### Important Variables 📝
- `percent`: Percentage change threshold for making buy/sell decisions. Change this value as needed.
- `peak`: Keeps track of the highest peak value during the analysis.
- `current_close`: Stores the most recent closing price.
- `is_buying`: Indicator of buying status (1 for buying, 0 for not buying).
- `indicator`: A value indicating whether to buy (1), sell (0), or hold (between 0 and 1) based on the percentage change.

### Final Decision 🚀📉
The script concludes by providing a final decision: Buy, Sell, or Hold, based on the calculated indicator value. The indicator value is a reflection of the percentage change from the peak value.

Feel free to customize and improve the script according to your needs and desired level of sophistication.

### Contribution 🙌 
Contributions are welcome! If you'd like to improve this script, fix any issues, or add new features, feel free to fork the repository and submit a pull request.

**⚠️Disclaimer:** It's important to note that this script serves educational and illustrative purposes solely. It does not guarantee profitable investment choices and should not be regarded as financial advice. Real investment decisions necessitate comprehensive considerations that go beyond historical price analysis. 📈📉
