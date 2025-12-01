import pandas as pd
import math


''' STUDY DESCRIPTION
Base Case: Buy $1000 worth of the SPY at market close every two weeks (every 10 trading days)
Backtesting Case: Every two weeks, receive $1000. If the SPY has retraced 20% from the highest point, buy the SPY. If not, add $1000 
to investing bucket. Deploy entire investing bucket every time the SPY has retraced 20%
Point of the study? Whose account is bigger at the end of the period
'''

# Bring in spy data with retracement column already calculated.
data = pd.read_csv("../data_set/backtesting_data.csv",parse_dates=["Date"])

# Define allowance and timing and retracement - assuming two weeks is roughly 10 trading days
allowance = 1000
period = 10
pullback_perc = -.2


# Add allowance column to data frame that will be populated every 10 trading days
data["Allowance"] = (data.index % period == 0).astype(int) * allowance

# Loop through dataframe and simulate results, will keep track of two different systems with two different dictionaries
base_case = {
    "shares": 0
}
backtesting_case = {
    "shares": 0,
    "bucket": 0
}

for i in range(len(data)):
    price = data.loc[i, "Adj Close"]
    allowance = data.loc[i, "Allowance"]
    retracement = data.loc[i,"Retracement"]
    if allowance:
        # handle our standard base case
        base_case["shares"] += math.floor(allowance / price)
        # add allowance to our bucket
        backtesting_case["bucket"] += allowance
    # handle bucket on retracement
    if retracement <= pullback_perc:
        backtesting_case["shares"] += math.floor(backtesting_case["bucket"] / price)
        # reset bucket to 0 as we have spent everything
        backtesting_case["bucket"] = 0


print(base_case)
print(backtesting_case)
print(data.tail())
