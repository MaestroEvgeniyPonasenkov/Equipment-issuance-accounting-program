"""
Программа для учёта выдачи оборудования
Автор: Ряднов Иван
Дата: 15.05.2023
"""
import os
import sys
from dotenv import load_dotenv
from emails.email_utils import get_mail
from emails.email_convertation import convert_email_to_dict
from emails.email_answers import location_error, approve_request, deny_request, alternative_request
from helpers.data_validation import validate_user, validate_location, validate_hardware
from helpers.db_api import fetch_requests, post_requests
from helpers.json_convertation import convert_data_to_json
from export.data_export import export_to_xlsx, export_to_docx


def account_equipment() -> None:
    """
    Функция для обработки электронного письма с запросом на выдачу оборудования. 

    Чтение данных авторизации из файла .env, получение  электронного письма 
    с помощью функции get_mail, преобразование полученных данных в словарь с 
    запросом request_data, проверка корректности указания локации в запросе с 
    использованием функции validate_location, проверка правильности данных 
    пользователя с использованием функции validate_user,  проверка корректности 
    указания запрашиваемого оборудования с помощью функции validate_hardware, 
    преобразование полученных данных в JSON и отправка их в базу данных с 
    помощью функции post_requests. 

    В случае, если данные заполнены неверно, пользователю высылается 
    соответствующий ответ на электронную почту. 

    Выход: None
    """
    load_dotenv()
    email_sender = os.getenv("EMAIL_SENDER")
    email_username = os.getenv("EMAIL_USERNAME")
    email_password = os.getenv("EMAIL_PASSWORD")

    try:
        request_email = get_mail(email_username, email_password)
    except ValueError as er:
            print(f"Error: {er}")
            sys.exit()
            
    request_data = convert_email_to_dict(request_email)

    try:
        validate_location(request_data)
    except ValueError:
        location_error(request_data, email_sender, email_username, email_password)
        sys.exit()
            
    user = validate_user(request_data)

    try:
        res = validate_hardware(request_data)
        if isinstance(res, tuple):
            json_data = convert_data_to_json(user, request_data, res)
            post_requests(json_data)
            approve_request(request_data, email_sender, email_username, email_password)
            sys.exit() 
        if isinstance(res, str):
            alternative_request(request_data, email_sender, email_username, email_password, res)
            sys.exit() 
    except TypeError:
        deny_request(request_data, email_sender, email_username, email_password)
        sys.exit()


def export_data(filename: str) -> None:
    """
    Функция для экспорта данных о запросах пользователей из базы в 
    форматы .xlsx и .docx. 

    Получение данных из базы данных с помощью функции fetch_requests, экспорт данных 
    в файлы форматов .xlsx и .docx с помощью функций export_to_xlsx и export_to_docx 
    соответственно. 

    Выход: None.
    """
    data = fetch_requests()
    export_to_docx(data, filename)
    export_to_xlsx(data, filename)


if __name__ == "__main__":
    account_equipment()
    export_data("user_requests")