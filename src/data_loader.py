import yfinance as yf
import pandas as pd
from pathlib import Path

DATA_PATH = Path("data") # Relative to project root

def download_spy(force=False):
    # Download historical data for SPY ETF if not already cached
    DATA_PATH.mkdir(exist_ok=True)
    file_path = DATA_PATH / "spy.csv"

    if file_path.exists() and not force:
        return pd.read_csv(file_path, parse_dates=["Date"], index_col="Date")
    
    df = yf.download("SPY", start="1993-01-01")
    df.to_csv(file_path)
    return df