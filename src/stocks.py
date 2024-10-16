import requests
import json
import os

ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')


def fetch_stock_data(stock_symbol: str, stock_api_key: str) -> dict:
    """Fetches the latest stock data from Alpha Vantage."""
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={
        stock_symbol}&apikey={stock_api_key}'
    response = requests.get(url, timeout=50)
    if response.status_code != 200:
        print(f"Error fetching stock data: {
              response.status_code} - {response.text}")
        return {}
    if 'Global Quote' not in response.json():
        return {}
    response.raise_for_status()
    data = response.json()
    data = data['Global Quote']
    return data


if __name__ == "__main__":
    stock_data = fetch_stock_data('AAPL', os.getenv('ALPHA_VANTAGE_API_KEY'))
    print(json.dumps(stock_data, indent=4))
