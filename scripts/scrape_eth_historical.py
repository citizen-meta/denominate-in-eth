# scripts/scrape_eth_historical.py

import yfinance as yf
import pandas as pd
import os

# Define ticker and date range
ticker = "ETH-USD"
start_date = "2015-01-01"

# Construct path to save CSV
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_file = os.path.join(project_root, "backend", "data", "eth_historical_data.csv")

# Fetch data
eth = yf.Ticker(ticker)
eth_data = eth.history(start=start_date)

# Save to CSV
eth_data.to_csv(output_file)
print(f"Saved {len(eth_data)} rows to {output_file}")
