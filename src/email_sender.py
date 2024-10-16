import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from news import fetch_news
from stocks import fetch_stock_data

# List of stock symbols
stock_symbols = ['AAPL', 'GOOGL', 'AMZN', 'MSFT', 'TSLA', 'META', 'NVDA']


def send_email(subject: str, body: str):
    """Sends an email with the specified subject and body."""
    EMAIL_CREDENTIALS = {
        "sender": os.getenv("EMAIL_USERNAME"),
        "recipient": os.getenv("EMAIL_RECIPIENT"),
        "password": os.getenv("EMAIL_PASSWORD"),
        "smtp_server": "smtp.gmail.com",
        "smtp_port": 587,
    }
    msg = MIMEMultipart("alternative")
    msg['From'] = EMAIL_CREDENTIALS['sender']
    msg['To'] = EMAIL_CREDENTIALS['recipient']
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))  # Attach as HTML content

    try:
        with smtplib.SMTP(EMAIL_CREDENTIALS['smtp_server'], EMAIL_CREDENTIALS['smtp_port']) as server:
            server.starttls()
            server.login(EMAIL_CREDENTIALS['sender'],
                         EMAIL_CREDENTIALS['password'])
            server.sendmail(
                EMAIL_CREDENTIALS['sender'], EMAIL_CREDENTIALS['recipient'], msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")


def create_email_content() -> tuple:
    """Creates the content for the email to be sent in HTML format."""
    subject = "Daily Stock Market Update 🎉"
    body = []

    stocks_api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
    news_api_key = os.getenv('NEWS_API_KEY')

    body.append("<html><body>")
    body.append("<h1>Daily Stock Market Update 🎉</h1>")

    for stock_symbol in stock_symbols:
        stock_data = fetch_stock_data(stock_symbol, stocks_api_key)
        stock_news_json = fetch_news(stock_symbol, news_api_key)

        body_element = f"<h2>{stock_symbol}</h2>"

        # Add stock data or error message
        if not stock_data:
            body_element += "<p>Error fetching stock data.</p>"
        else:
            body_element += f"""
            <p><strong>Open:</strong> {stock_data['02. open']}<br>
            <strong>Price:</strong> {stock_data['05. price']}<br>
            <strong>Change:</strong> {stock_data['09. change']} ({stock_data['10. change percent']})</p>
            """

        # Always add the news section
        body_element += "<h3>Related News:</h3><ul>"
        image_added = False  # To track if we've added an image

        for news in stock_news_json:  # Assuming stock_news_json is a list of news articles
            body_element += f"<li><strong>{news['title']}</strong><br>"
            body_element += f"<p>{news['description']
                                  }<br><a href='{news['url']}'>Read more</a></p></li>"

            # Check for an image in the current news item
            if 'urlToImage' in news and not image_added:  # Only add the first image found
                image_url = news['urlToImage']
                body_element += f"""
                <div style='text-align: center;'>
                    <img src='{image_url}' alt='News Image' width='200' style='border-radius: 5px;'>
                </div>
                """
                image_added = True  # Mark that we've added an image

        body_element += "</ul>"
        body_element += "<hr>"
        body.append(body_element)

    body.append("</body></html>")
    body_string = "".join(body)
    return subject, body_string


# Main block to send the email
if __name__ == "__main__":
    subject, body = create_email_content()
    send_email(subject, body)
