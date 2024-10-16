import requests
from dotenv import load_dotenv
import json
import os

load_dotenv()

NEWS_API_KEY = os.getenv('NEWS_API_KEY')
ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')


def fetch_news(stock_symbol: str) -> str:
    """Fetches the latest news articles related to the stock symbol."""
    url = f'https://newsapi.org/v2/everything?q={
        stock_symbol}&apiKey={NEWS_API_KEY}'
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error fetching news: {response.status_code} - {response.text}")
        return []

    articles = response.json().get('articles', [])

    # Filter out articles that are empty or contain '[Removed]' in any of the relevant fields
    filtered_articles = []
    for article in articles:
        if article.get('title') and article.get('description') and '[Removed]' not in article.get('title') and '[Removed]' not in article.get('description'):
            filtered_articles.append(article)
    # Return the top 3 filtered articles
    return filtered_articles[0]


if __name__ == "__main__":
    news_data = fetch_news('AAPL')
    print(json.dumps(news_data, indent=4))
