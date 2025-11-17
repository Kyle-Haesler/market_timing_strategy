import os
import yfinance as yf

# Yahoofinance download inputs
ticker = "SPY"
interval = "1d"

# Download data from Yahoofinance and polish DataFrame
data = yf.download(ticker, period="max", interval=interval, auto_adjust=False)
data.columns = data.columns.droplevel(1)
data.columns.name = None
data.reset_index(inplace=True)

# Ensure data folder exists
os.makedirs("../data", exist_ok=True)

save_path = "../data/spy.csv"

# Save the data in a CSV file
data.to_csv(save_path, index=False)

print(f"\n Data saved successfully to {save_path}")
