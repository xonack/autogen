# python code
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the US top 10 companies by market cap (They might vary time to time)
companies = ["AAPL", "MSFT", "AMZN", "GOOG", "GOOGL", "FB", "BRK-A", "V", "JNJ", "WMT"]

# Collect the P/E ratios and market caps
data = {}
for company in companies:
    ticker = yf.Ticker(company)
    info = ticker.info
    data[company] = {
        "PE Ratio": info.get("trailingPE", "N/A"), 
        "Market Cap": info.get("marketCap", "N/A"), 
        "Name": info["shortName"]
    }

# Create a pandas dataframe from the data
df = pd.DataFrame.from_dict(data, orient="index")

# Filter out the rows where PE Ratio or Market Cap is "N/A"
df = df[(df['PE Ratio'] != "N/A") & (df['Market Cap'] != "N/A")]

# Sort the dataframe by market cap
df = df.sort_values(by="Market Cap", ascending=False)

# Plot the P/E Ratios
plt.bar(df["Name"], df["PE Ratio"])
plt.xlabel('Company')
plt.xticks(rotation=90)
plt.ylabel('P/E Ratio')
plt.title('P/E Ratio of the 10 Largest US Companies by Market Cap')
plt.show()
