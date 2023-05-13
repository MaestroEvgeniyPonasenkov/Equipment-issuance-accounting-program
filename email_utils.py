import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import python_version
from validate_email import validate_email
import imaplib
import email


def send_email(text: str, recipient: str, subject: str, email_name: str, email_password: str, template=None,
               name: str = None) -> None:
    """
    Sending an email.

    Args:
        text: str -> a text message to send in the email
        recipient: str -> the email of the recipient
        subject: str -> the subject of the email
        email_name: str -> the sender email address
        email_password: str -> the password to the sender email address
        template: str -> an optionale predfined html mail template
        name: str -> the name of the sender

    Returns:
        print message: 'The email was sent successfully!' if the email send was successful.

    Raises:
        ValueError: this error is raised if the email of the recipient is not valid
        Exception: this error is raised if there was an error that occured while sending the email
    """
    try:
        if not validate_email(recipient):
            raise ValueError("This email does not exist")

        if template:
            with open(template) as file:
                templ = file.read()
        else:
            templ = f"<html><head></head><body><p>{text}</p></body></html>"

        server = "smtp.yandex.ru"
        html = templ
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
        print("The email was sent successfully!")

    except ValueError as e:
        print(str(e))

    except Exception as e:
        print(f"An error occurred while sending an email: {e}")


def get_email(email_name: str, email_password: str) -> str:
    """
    Reading the latest email.

    Args:
        email_name: str -> the email address that you want to read the inbox messages
        email_password: str -> the password to the email address

    Returns:
        result: str -> the latest emails message text if available else, a string with an error message.
    """
    try:
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
    except Exception as e:
        return f"An error occurred while reading email: {e}"


# Before using the program you should allow mailbox access with email clients
try:
    user = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()
except Exception:
    print("Incorrect email or password")
rec = input("Enter your recipient: ").strip()
sub = input("Enter subject: ").strip()
txt = input("Enter message: ").strip()
send_email(text=txt, recipient=rec, subject=sub,
           email_name=user, email_password=password)
get_email(email_name=user, email_password=password)
