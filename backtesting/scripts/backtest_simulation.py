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
pullback_perc = -.01


# Add allowance column to data frame that will be populated every 10 trading days
data["Allowance"] = (data.index % period == 0).astype(int) * allowance

# Loop through dataframe and simulate results, will keep track of two different systems with two different dictionaries
base_case = {
    "shares": 0,
    "bucket": 0
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
        # give both of our buckets the allowance
        base_case["bucket"] += allowance
        backtesting_case["bucket"] += allowance
        # handle our standard base case
        base_shares = math.floor(base_case["bucket"] / price)
        base_case["shares"] += base_shares
        base_capital_spent = base_shares * price
        # subtract out capital spent from base bucket (handles leftover cash)
        base_case["bucket"] -= base_capital_spent
    # handle bucket on retracement
    if retracement <= pullback_perc and backtesting_case["bucket"] > 0:
        backtesting_shares = math.floor(backtesting_case["bucket"] / price)
        backtesting_case["shares"] += backtesting_shares
        backtesting_capital_spent = backtesting_shares * price
        # subtract out capital spent from backtesting bucket (handles leftover cash)
        backtesting_case["bucket"] -= backtesting_capital_spent
        
final_price = data["Adj Close"].iloc[-1]
base_case["Total Value"] = (base_case["shares"] * final_price) + base_case["bucket"]
backtesting_case["Total Value"] = (backtesting_case["shares"] * final_price) + backtesting_case["bucket"]

print(base_case)
print(backtesting_case)
print(data.tail())
