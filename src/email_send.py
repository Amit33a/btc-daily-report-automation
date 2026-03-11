import smtplib
from email.message import EmailMessage
from src.config import get_settings


def send_email(subject: str, body: str):

    settings = get_settings()

    msg = EmailMessage()
    msg["From"] = settings.email_from
    msg["To"] = settings.email_to
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP(settings.smtp_host, settings.smtp_port, timeout=30) as smtp:

        smtp.ehlo()

        smtp.starttls()

        smtp.ehlo()

        smtp.login(settings.email_from, settings.email_app_password)

        smtp.send_message(msg)