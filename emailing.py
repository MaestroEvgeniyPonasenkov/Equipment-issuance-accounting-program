import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import python_version
from validate_email import validate_email
import imaplib
import email


def send_email(text: str, recipient: str, subject: str, email_name: str, email_password: str, template=None,
               name: str = None) -> str:
    """Sending an email on mail.yandex"""

    if not validate_email(recipient):
        raise ValueError("This email does not exist")
    if template:
        try:
            with open(template) as file:
                templ = file.read()
        except IOError:
            return "The template file doesn't found!"
    server = "smtp.yandex.ru"
    html = templ if template else f"<html><head></head><body><p>{text}</p></body></html>"
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"{name} <{email_name}>" if name else email_name
    msg["To"] = recipient
    msg["Reply-To"] = email_name
    msg["Return-Path"] = email_name
    msg["X-Mailer"] = f"Python/{(python_version())}"
    part_text = MIMEText(text, "plain")
    part_html = MIMEText(html, "html")
    msg.attach(part_text)
    msg.attach(part_html)
    mail = smtplib.SMTP_SSL(server)
    mail.login(email_name, email_password)
    mail.sendmail(email_name, recipient, msg.as_string())
    mail.quit()
    return "The email was sent successfully!"


def get_email(email_name: str, email_password: str) -> str:
    """Reading the latest email on mail.yandex"""

    mail = imaplib.IMAP4_SSL("imap.yandex.ru")
    mail.login(email_name, email_password)
    mail.select("inbox")
    _, data = mail.search(None, "ALL")
    id_list = data[0].split()
    latest_email_id = id_list[-1]
    _, data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email)
    result = email_message.get_payload()
    mail.close()
    return result


# Before using the program you should allow mailbox access with email clients
try:
    user = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()
except Exception:
    print("Incorrect email or password")
rec = input("Enter your recipient: ").strip()
sub = input("Enter subject: ").strip()
txt = input("Enter message: ").strip()
print(send_email(txt, rec, sub, user, password))
print(get_email(user, password))
