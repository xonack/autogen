import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "yfinance"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])
# Required Libraries
import yfinance as yf
import matplotlib.pyplot as plt



# Stock Symbols
nvda_symbol = "NVDA"
tesla_symbol = "TSLA"

# Fetching Stock Data
nvda_data = yf.download(nvda_symbol, start="2022-01-01")
tesla_data = yf.download(tesla_symbol, start="2022-01-01")

# Extracting YTD Stock Price Change
nvda_ytd_change = nvda_data["Close"].pct_change().cumsum()
tesla_ytd_change = tesla_data["Close"].pct_change().cumsum()

# Plotting the Chart
plt.figure(figsize=(12, 6))
plt.plot(nvda_ytd_change.index, nvda_ytd_change, label="NVDA")
plt.plot(tesla_ytd_change.index, tesla_ytd_change, label="TSLA")
plt.title("NVDA and TSLA Stock Price Change YTD")
plt.xlabel("Date")
plt.ylabel("Stock Price Change (%)")
plt.legend()
plt.grid(True)
plt.show()
