import requests
import os

ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')


def fetch_stock_data(stock_symbol: str) -> dict:
    """Fetches the latest stock data from Alpha Vantage."""
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={
        stock_symbol}&apikey={ALPHA_VANTAGE_API_KEY}'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    stock_data = data['Global Quote']
    return stock_data
