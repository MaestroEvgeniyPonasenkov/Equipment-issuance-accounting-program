"""
Программа для учёта выдачи оборудования
Автор: Ряднов Иван
Дата: 15.05.2023
"""
from dotenv import load_dotenv
import os

from helpers.data_validation import validate_user, validate_location, validate_hardware
from helpers.db_api import post_requests
from helpers.json_convertation import convert_data_to_json
from emails.email_utils import get_mail
from emails.email_convertation import convert_email_to_dict
from emails.email_answers import location_error, approve_request, deny_request, alternative_request, db_error


def get_data(email_username: str, email_password: str) -> list[str]:
    """
    Функция для получения списка новых сообщений из электронной почты.
    Параметры:
    - email_username (str): логин пользователя электронной почты.
    - email_password (str): пароль от учетной записи пользователя.

    Возвращает список `messages` email сообщений, полученных с
    сервера почтовой службы.

    Если новых сообщений нет, то печатает 'На данный момент новых
    запросов нет' и завершает программу.

    Выход: список строк `messages`.
    """
    try:
        messages = get_mail(email_username, email_password)
        return messages
    except ValueError:
        return []


def account_equipment(request_data: dict, email_sender: str, email_username: str, email_password: str) -> None:
    """
    Функция для обработки электронного письма с запросом на выдачу оборудования.

    Чтение данных, проверка корректности указания локации в запросе с
    использованием функции validate_location, проверка правильности данных
    пользователя с использованием функции validate_user, проверка корректности
    указания запрашиваемого оборудования с помощью функции validate_hardware,
    преобразование полученных данных в JSON и отправка их в базу данных с
    помощью функции post_requests.

    В случае, если данные заполнены неверно, пользователю высылается
    соответствующий ответ на электронную почту.

    Выход: None
    """
    try:
        request_data.update({'Номер_аудитории': request_data.get('Аудитория')})
        request_data.update({'Аудитория': validate_location(request_data)})
    except ValueError:
        location_error(request_data, email_sender, email_username, email_password)
        return

    user = validate_user(request_data)

    try:
        res = validate_hardware(request_data)
        if isinstance(res, tuple):
            json_data = convert_data_to_json(user, request_data, res)
            request_res = post_requests(json_data)
            if request_res:
                approve_request(request_data, email_sender, email_username, email_password)
            else:
                db_error(request_data, email_sender, email_username, email_password)
            return
        if isinstance(res, str):
            alternative_request(request_data, email_sender, email_username, email_password, res)
            return
    except TypeError:
        deny_request(request_data, email_sender, email_username, email_password)
        return


def start():
    path = os.getcwd()
    load_dotenv(f'{path}/.env')
    email_sender = os.getenv("EMAIL_SENDER")
    email_username = os.getenv("EMAIL_USERNAME")
    email_password = os.getenv("EMAIL_PASSWORD")

    messages = get_data(email_username, email_password)
    if not messages:
        return "На данный момент новых запросов нет"

    for message in messages:
        message_parsed = convert_email_to_dict(message)
        account_equipment(message_parsed, email_sender, email_username, email_password)
    return f"Было обработано {len(messages)} запросов"
