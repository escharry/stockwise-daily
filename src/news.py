import requests
from dotenv import load_dotenv
import json
import os


def fetch_news(stock_symbol: str, news_api_key: str) -> str:
    """Fetches the latest news articles related to the stock symbol."""
    url = f'https://newsapi.org/v2/everything?q={
        stock_symbol}&apiKey={news_api_key}'
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
    news_data = fetch_news('AAPL', os.getenv('NEWS_API_KEY'))
    print(json.dumps(news_data, indent=4))
