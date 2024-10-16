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
    msg.attach(MIMEText(body, 'plain'))

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
    """Creates the content for the email to be sent in plain text."""
    subject = "Daily Stock Market Update 🎉"
    body = []

    for stock_symbol in stock_symbols:
        stock_data = fetch_stock_data(stock_symbol)
        stock_news_json = fetch_news(stock_symbol)

        if not stock_data:
            body_element = f"Error fetching data for {stock_symbol}\n"
            for key in stock_news_json:
                if key == 'source':
                    body_element += f"{key}: {stock_news_json[key]['name']}\n"
                else:
                    body_element += f"{key}: {stock_news_json[key]}\n"
            body.append(body_element + "\n")
        else:
            body_element = f"""
            {stock_data['01. symbol']}:
            Open: {stock_data['02. open']}
            Price: {stock_data['05. price']}
            Change: {stock_data['09. change']} (
                {stock_data['10. change percent']})

            Related News:
            """
            for key in stock_news_json:
                body_element += f"{key}: {stock_news_json[key]}\n"

            body.append(body_element + "\n")

    body_string = "".join(body)
    return subject, body_string


# Main block to send the email
if __name__ == "__main__":
    subject, body = create_email_content()
    send_email(subject, body)
