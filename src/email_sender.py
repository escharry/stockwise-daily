import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from news import fetch_news
from stocks import fetch_stock_data

# Function to send an email


def send_email(subject: str, body: str) -> None:
    """Sends an email with the given subject and body."""
    EMAIL_CREDENTIALS = {
        # Get email from environment variable
        "sender": os.getenv("EMAIL_USERNAME"),
        "recipient": os.getenv("EMAIL_RECIPIENT"),
        "password": os.getenv("EMAIL_PASSWORD"),
        "smtp_server": "smtp.gmail.com",  # Use your SMTP server
        "smtp_port": 587,  # Use TLS
    }

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = EMAIL_CREDENTIALS['sender']
    msg['To'] = EMAIL_CREDENTIALS['recipient']
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        with smtplib.SMTP(EMAIL_CREDENTIALS['smtp_server'], EMAIL_CREDENTIALS['smtp_port']) as server:
            server.starttls()  # Secure the connection
            # Login using the environment variable for the password
            server.login(EMAIL_CREDENTIALS['sender'],
                         EMAIL_CREDENTIALS['password'])
            server.sendmail(
                EMAIL_CREDENTIALS['sender'], EMAIL_CREDENTIALS['recipient'], msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Example function to create the email content


def create_email_content() -> tuple:
    """Creates the content for the email to be sent."""
    subject = "Daily Stock Market Update"
    body = "This is your daily update including stock market news and a random fact."
    return subject, body


# Main block to send the email
if __name__ == "__main__":
    subject, body = create_email_content()
    send_email(subject, body)
