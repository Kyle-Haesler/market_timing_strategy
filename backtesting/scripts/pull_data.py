import pandas as pd

# bring in data from retracement folder 
data = pd.read_csv("../../retracement/data_set/retracement_analysis_data.csv", parse_dates=["Date"])

# Add dataset as csv to backtesting folder 
data.to_csv("../data_set/backtesting_data.csv", index=False)

print(f"Backtesting data saved to data_set folder")