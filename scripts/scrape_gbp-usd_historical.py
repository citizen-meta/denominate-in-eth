# scripts/scrape_gbp_usd_historical.py

import yfinance as yf
import os

# Define ticker and date range
ticker = "GBPUSD=X"  # Yahoo Finance ticker for GBP/USD
start_date = "2015-01-01"

# Resolve output path
output_file = os.path.expanduser("~/denominate-in-eth/backend/data/gbp_usd_historical.csv")

# Fetch data
gbp_usd = yf.Ticker(ticker)
exchange_data = gbp_usd.history(start=start_date)

# Save to CSV
exchange_data.to_csv(output_file)
print(f"Saved {len(exchange_data)} rows to {output_file}")
