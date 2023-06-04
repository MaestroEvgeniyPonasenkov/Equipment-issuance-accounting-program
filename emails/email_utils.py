import smtplib
import imaplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def decode_email(message) -> str:
    """
    Function to decode email message.

    Args:
        message (email.message.Message): email message to be decoded.

    Returns:
        str: decoded text of the email message
    """
    text = ""
    if message.is_multipart():
        for part in message.walk():
            content_type = part.get_content_type()
            if content_type == "text/plain" or content_type == "text/html":
                text += part.get_payload(decode=True).decode("utf-8")
    else:
        text = message.get_payload(decode=True).decode("utf-8")
    return text


def send_email(subject: str, body: str, recipient: str, email_sender: str, email_username: str,
               email_password: str) -> None:
    """
    Function to send an email message using SMTP and MIMEText libraries.

    Args:
        subject (str): subject of the email message.
        body (str): body of the email message.
        recipient (str): recipient email address.
        email_sender (str): name of the email sender.
        email_username (str): username of the email sender.
        email_password (str): password of the email sender.

    Returns:
        None
    """
    smtp_server = "smtp.yandex.ru"
    message = MIMEMultipart()
    message['From'] = f"{email_sender} <{email_username}>"
    message['To'] = recipient
    message['Subject'] = subject
    message.attach(MIMEText(body, 'html'))
    try:
        mail = smtplib.SMTP_SSL(smtp_server)
        mail.login(email_username, email_password)
        mail.sendmail(email_username, recipient, message.as_string())
        mail.quit()
        print("Письмо успешно отправлено!")
    except Exception as e:
        print("Ошибка при отправке письма:", str(e))


def get_mail(email_username: str, email_password: str) -> list[str]:
    """
    This function logs into the email box using given
    email_username and email_password. It then returns the
    plain text of the latest email.

    Args:
        email_username: Email ID to log in
        email_password: Password for email account

    Returns:
        str: List of plain texts of the email message
    """
    smtp_server = "imap.yandex.ru"
    mail = imaplib.IMAP4_SSL(smtp_server)
    mail.login(email_username, email_password)
    mail.select("inbox")
    subject = "New equipment request"
    search_criteria = f'(UNSEEN SUBJECT "{subject}")'
    _, data = mail.search(None, search_criteria)
    email_ids = data[0].split()
    if not email_ids:
        raise ValueError(
            "На данный момент новых запросов нет")
    messages = []
    for email_id in email_ids:
        _, data = mail.fetch(email_id, "(RFC822)")
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)
        result = decode_email(email_message)
        messages.append(result)
        mail.store(email_id, '+FLAGS', '\\Seen')
    mail.logout()
    return messages