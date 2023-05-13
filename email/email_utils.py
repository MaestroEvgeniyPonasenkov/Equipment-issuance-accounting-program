import smtplib
import imaplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from validate_email import validate_email


def parse_email_message(email_message) -> str:
    """
    This function extracts the plain text from email_message and 
    returns it as string.

    Args:
        email_message: email message to extract text from

    Returns:
        str: Parsed text of the email message
    """
    message_text = ""
    if email_message.is_multipart():
        for part in email_message.get_payload():
            if part.get_content_type() == "text/plain":
                message_text = part.get_payload(decode=True).decode('utf-8')
                break
    else:
        message_text = email_message.get_payload(decode=True).decode('utf-8')
    if isinstance(message_text, bytes):
        message_text = message_text.decode()
    return message_text


def send_email(subject: str, body: str, recipient: str, email_sender: str, email_username: str, email_password: str) -> None:
    """
    Send an email message using SMTP and MIMEText libraries.

    :param subject: Subject of the email message.
    :type subject: str
    :param body: Body of the email message.
    :type body: str
    :param recipient: Recipient email address.
    :type recipient: str
    :param email_sender: Name of the email sender.
    :type email_sender: str
    :param email_username: Username of the email sender.
    :type email_username: str
    :param email_password: Password of the email sender.
    :type email_password: str
    :return: None
    :rtype: None
    """
    if not validate_email(recipient):
        raise ValueError("This email does not exist")
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


def get_mail(email_username: str, email_password: str) -> str:
    """
    This function logs into the email box using given
    email_username and email_password. It then returns the
    plain text of the latest email.

    Args:
        email_username: Email ID to log in
        email_password: Password for email account

    Returns:
        str: Plain text of the email message
    """
    smtp_server = "imap.yandex.ru"
    mail = imaplib.IMAP4_SSL(smtp_server)
    mail.login(email_username, email_password)
    mail.select("inbox")
    _, data = mail.search(None, "ALL")
    latest_email_id = data[0].split()[-1]
    _, data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email)
    result = parse_email_message(email_message)
    mail.close()
    return result
