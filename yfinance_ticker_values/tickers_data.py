import yfinance
import yfinance as yf
import pandas as pd
import datetime

# List of stock tickers
tickers = [
    'AMZN', 'GOOG', 'META', 'NVDA', 'FSKAX',
    'FXAIX', 'QQQ', 'VGT', 'VTI', 'FTIHX'
]

# Define start and end dates
start_date = '2020-08-17'
end_date = '2025-08-16'

print(f"[{datetime.datetime.now()}] Starting download for tickers: {tickers}")
print(f"[{datetime.datetime.now()}] Number of tickers: {len(tickers)}")
print(f"[{datetime.datetime.now()}] Date range: {start_date} to {end_date}")

# Download historical Adjusted Close prices with error handling
try:
    data = yf.download(
        tickers,
        start=start_date,
        end=end_date,
        auto_adjust=False
    )['Adj Close']
    print(
        f"[{datetime.datetime.now()}] Download successful. "
        f"Data shape: {data.shape}"
    )
    print(data.head())
    csv_filename = 'portfolio_historical_data.csv'
    data.to_csv(csv_filename)
    print(
        f"[{datetime.datetime.now()}] Data saved to "
        f"'{csv_filename}'"
    )
except Exception as e:
    print(
        f"[{datetime.datetime.now()}] Error downloading data: {e}"
    )