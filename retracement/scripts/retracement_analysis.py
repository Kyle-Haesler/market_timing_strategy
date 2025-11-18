import pandas as pd

# bring in spy.csv data
data = pd.read_csv("../../data/spy.csv", parse_dates=["Date"])

# Add max high & retracement column to DataFrame
data["Max High"] = data["High"].cummax()
data["Retracement"] = (data["Low"] - data["Max High"]) / data["Max High"] 


# Add dataset as csv to data_set folder
data.to_csv("../data_set/retracement_analysis_data.csv", index=False)

print(f"Retracement data saved to data_set folder")