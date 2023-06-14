import os
from jinja2 import Environment, FileSystemLoader
from . import email_utils


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
    path = f"{os.getcwd()}\\emails\\templates"
    env = Environment(loader=FileSystemLoader(path))
    template = env.get_template(template_name)
    return template.render(**kwargs)


def approve_request(user_data: dict, email_sender: str, email_username: str, email_password: str) -> None:
    """
    Одобрение выдачи прошиваемой платы

    Параметры:
    - user (str): Имя пользователя
    - approved_subject (str): Тема письма об одобрении запроса на выдачу платы
    - approved_template (str): Путь до шаблона письма об одобрении запроса
    - approved_data (dict): Словарь с данными для запроса
        Ожидаемые ключи:
        - recipient_name (str): Имя получателя
        - user_number (str): Номер пользователя
        - location (str): Местоположение пользователя
        - issue_date (str): Дата выдачи платы
        - issue_return (str): Дата возврата платы
        - issued_by (str): Кем выдана плата
        - comment (str): Комментарий к запросу
        - hardware (list): Список просимых плат
        - contact_person (str): Имя контактного лица
        - your_name (str): Ваше имя
    - approved_body (str): Сгенерированная разметка письма
    """
    approved_subject = "Одобрение запроса на выдачу программируемой платы"
    approved_template = 'approved_template.html'
    approved_data = {
        'recipient_name': f"{user_data.get('Имя')} {user_data.get('Фамилия')}",
        'location': user_data.get('Номер_аудитории'),
        'issue_date': user_data.get('Дата_выдачи'),
        'return_date': user_data.get('Дата_возврата'),
        'hardware': user_data.get('Плата'),
        'contact_person': 'vzunin@hse.ru',
        'your_name': 'МИЭМ',
    }
    approved_body = render_template(approved_template, **approved_data)
    email_utils.send_email(approved_subject, approved_body, user_data.get('Почта'),
                           email_sender, email_username, email_password)


def deny_request(user_data: dict, email_sender: str, email_username: str, email_password: str) -> None:
    """
    Отказ в запросе на выдачу программируемой платы

    Параметры:
    - user (str): Имя пользователя
    - denied_subject (str): Тема письма об отказе в запросе
    - denied_template (str): Путь до шаблона письма
    - denied_data (dict): Словарь с данными для запроса
        Ожидаемые ключи:
        - recipient_name (str): Имя получателя
        - contact_person (str): Имя контактного лица
        - your_name (str): Ваше имя
    - denied_body (str): Сгенерированная разметка письма
    """
    denied_subject = "Отказ в запросе на выдачу программируемой платы"
    denied_template = 'denied_template.html'
    denied_data = {
        'recipient_name': f"{user_data.get('Имя')} {user_data.get('Фамилия')}",
        'hardware': user_data.get('Плата'),
        'quantity': user_data.get('Количество'),
        'contact_person': 'vzunin@hse.ru',
        'your_name': 'МИЭМ',
    }
    denied_body = render_template(denied_template, **denied_data)
    email_utils.send_email(denied_subject, denied_body, user_data.get('Почта'),
                           email_sender, email_username, email_password)


def alternative_request(user_data: dict, email_sender: str, email_username: str, email_password: str,
                        alternative: str) -> None:
    """
    Информация об альтернативной плате

    Параметры:
    - user (str): Имя пользователя
    - alternative_subject (str): Тема письма с инф-ей об альтернативной плате
    - alternative_template (str): Путь до шаблона письма
    - alternative_data (dict): Словарь с данными для запроса
        Ожидаемые ключи:
        - recipient_name (str): Имя получателя
        - alternatives (list): Список альтернативных плат
            - name (str): Название платы
        - contact_person (str): Имя контактного лица
        - your_name (str): Ваше имя
    - alternative_body (str): Сгенерированная разметка письма
    """
    alternative_subject = "Информация об альтернативной плате"
    alternative_template = 'alternative_template.html'
    alternative_data = {
        'recipient_name': f"{user_data.get('Имя')} {user_data.get('Фамилия')}",
        'alternatives': alternative,
        'contact_person': 'vzunin@hse.ru',
        'your_name': 'МИЭМ'
    }
    alternative_body = render_template(alternative_template, **alternative_data)
    email_utils.send_email(alternative_subject, alternative_body, user_data.get('Почта'),
                           email_sender, email_username, email_password)


def location_error(user_data: dict, email_sender: str, email_username: str, email_password: str) -> None:
    """
    Generate an email to inform the recipient that the location error has occurred.

    Parameters:

    user (str): The name of the user
    locationerror_subject (str): The subject of the email
    locationerror_template (str): The path to the email template
    locationerror_data (dict): A dictionary with the following keys:
    recipient_name (str): The name of the person receiving the email
    contact_person (str): The name of the contact person
    your_name (str): Your name or the name of the person writing the email
    locationerror_body (str): The generated email body

    Returns:
        None
    """
    locationerror_subject = "Ошибка в запросе на выдачу программируемой платы"
    locationerror_template = 'locationerror_template.html'
    locationerror_data = {
        'recipient_name': f"{user_data.get('Имя')} {user_data.get('Фамилия')}",
        'contact_person': 'vzunin@hse.ru',
        'your_name': 'МИЭМ'
    }
    locationerror_body = render_template(locationerror_template, **locationerror_data)
    email_utils.send_email(locationerror_subject, locationerror_body, user_data.get('Почта'),
                           email_sender, email_username, email_password)


def db_error(user_data: dict, email_sender: str, email_username: str, email_password: str) -> None:
    """
    Generate an email to inform the recipient that the database error has occurred.

    Parameters:

    user (str): The name of the user
    dberror_subject (str): The subject of the email
    dberror_template (str): The path to the email template
    dberror_data (dict): A dictionary with the following keys:
    recipient_name (str): The name of the person receiving the email
    contact_person (str): The name of the contact person
    your_name (str): Your name or the name of the person writing the email
    dberror_body (str): The generated email body

    Returns:
        None
    """
    dberror_subject = "Ошибка при работе с базой данных"
    dberror_template = 'dberror_template.html'
    dberror_data = {
        'recipient_name': f"{user_data.get('Имя')} {user_data.get('Фамилия')}",
        'contact_person': 'vzunin@hse.ru',
        'your_name': 'МИЭМ'
    }
    dberror_body = render_template(dberror_template, **dberror_data)
    email_utils.send_email(dberror_subject, dberror_body, user_data.get('Почта'),
                           email_sender, email_username, email_password)
