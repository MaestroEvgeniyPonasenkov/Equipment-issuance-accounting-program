import os
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
from email_utils import send_email


def render_template(template_name: str, **kwargs) -> str:
    """
    Render a template using Jinja2 library.

    :param template_name: Name of the template to be rendered.
    :type template_name: str
    :param kwargs: Data to be provided to the template.
    :type kwargs: dict
    :return: Rendered template output.
    :rtype: str
    """
    path = f"{os.getcwd()}\\email\\templates"
    env = Environment(loader=FileSystemLoader(path))
    template = env.get_template(template_name)
    return template.render(**kwargs)


def approve_request():
    user = ''
    approved_subject = "Одобрение запроса на выдачу программируемой платы"
    approved_template = 'approved_template.html'
    approved_data = {
        'recipient_name': '',
        'user_number': '',
        'location': '',
        'issue_date': '',
        'issue_return': '',
        'issued_by': '',
        'comment': '',
        'hardware': ['plata1', 'plata2'],
        'contact_person': '',
        'your_name': ''
    }
    approved_body = render_template(approved_template, **approved_data)
    send_email(approved_subject, approved_body, user,
           email_sender, email_username, email_password)


def deny_request():
    user = ''
    denied_subject = "Отказ в запросе на выдачу программируемой платы"
    denied_template = 'denied_template.html'
    denied_data = {
        'recipient_name': 'Имя получателя',
        'contact_person': '',
        'your_name': ''
    }
    denied_body = render_template(denied_template, **denied_data)
    send_email(denied_subject, denied_body, user,
           email_sender, email_username, email_password)

    
def alternative_request():
    user = ''
    alternative_subject = "Информация об альтернативной плате"
    alternative_template = 'alternative_template.html'
    alternative_data = {
        'recipient_name': 'Имя получателя',
        'alternatives': [
            {'name': 'Альтернативная плата 1'},
            {'name': 'Альтернативная плата 2'}
        ],
        'contact_person': '',
        'your_name': ''
    }
    alternative_body = render_template(alternative_template, **alternative_data)
    send_email(alternative_subject, alternative_body, user,
           email_sender, email_username, email_password)


load_dotenv()
email_sender = os.getenv("EMAIL_SENDER")
email_username = os.getenv("EMAIL_USERNAME")
email_password = os.getenv("EMAIL_PASSWORD")
approve_request()
deny_request()
alternative_request()