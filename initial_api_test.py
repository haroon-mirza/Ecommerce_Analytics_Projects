import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
alpha_vantage_key = os.getenv('alpha_vantage_key')

# Setting up the call
url = "https://www.alphavantage.co/query"
params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": "MSFT",
    "interval": "5min",
    "apikey": alpha_vantage_key
}

# API call
response = requests.get(url, params=params)

# Parse the JSON response
data = json.loads(response.text)

# Print the latest stock data (for testing purposes)
latest_data = data["Time Series (5min)"]
latest_timestamp = list(latest_data.keys())[0]
print("Latest data for MSFT at {}: {}".format(latest_timestamp, latest_data[latest_timestamp]))
