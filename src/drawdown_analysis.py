import pandas as pd

def calculate_drawdowns(prices: pd.Series) -> pd.Series:
    """
    Calculate drawdowns as % from previous rolling high.
    Returns a series of drawdown percentages (negative values).
    """
    rolling_high = prices.cummax()
    drawdowns = (prices / rolling_high) - 1
    return drawdowns