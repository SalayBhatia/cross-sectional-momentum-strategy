import yfinance as yf
import pandas as pd

def load_data(tickers, start_date, end_date=None):
    data = yf.download(
        tickers,
        start=start_date,
        end=end_date,
        auto_adjust=False,
        progress=False
    )
    
    prices = data["Adj Close"]
    return prices

