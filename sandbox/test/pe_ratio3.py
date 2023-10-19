# python code
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

try:
    # Define the US top 10 companies by market cap (They might vary time to time)
    # Details could be changed time to time
    companies = ["AAPL", "MSFT", "AMZN", "GOOG", "GOOGL", "FB", "BRK-A", "V", "JNJ", "WMT"]

    # Collect the P/E ratios and market caps
    data = {}
    for company in companies:
        try:
            ticker = yf.Ticker(company)
            info = ticker.info
            # Check for missing values and handle respectively
            pe_ratio = info["trailingPE"] if "trailingPE" in info else "N/A"
            market_cap = info["marketCap"] if "marketCap" in info else "N/A"
            short_name = info["shortName"] if "shortName" in info else "N/A"

            data[company] = {"PE Ratio": pe_ratio, "Market Cap": market_cap, "Name": short_name}
        
        except Exception as e:
            print("Error occurred while fetching data for company '{}': {}\n".format(company, str(e)))
            continue

    # Create a pandas dataframe from the data
    df = pd.DataFrame.from_dict(data, orient="index")

    # Sort the dataframe by market cap
    df = df[df["Market Cap"] != "N/A"].sort_values(by="Market Cap", ascending=False)

    # Plot the P/E Ratios of the companies for which it's available
    df_without_na = df[df["PE Ratio"] != "N/A"]
    plt.bar(df_without_na["Name"], df_without_na["PE Ratio"])
    plt.xlabel('Company')
    plt.xticks(rotation=90)
    plt.ylabel('P/E Ratio')
    plt.title('P/E Ratio of the 10 Largest US Companies by Market Cap')
    plt.show()
    
except Exception as e:
    print("Error occurred: ", str(e))
