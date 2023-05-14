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
from emails.email_validation import validate_user, validate_location, validate_hardware
from emails.email_answers import location_error, approve_request, deny_request, alternative_request
from export.data_export import export_to_xlsx, export_to_docx
from db_api import fetch_requests, post_requests
from json_convertation import convert_data_to_json


def main():
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
        try:
            user_email = request_data.get('Почта')
            user_fullname = f"{request_data.get('Имя')} {request_data.get('Фамилия')}"
            location_error(user_email, user_fullname, email_sender, email_username, email_password)
            sys.exit()
        except ValueError as er:
            print(f"Error: {er}")
            sys.exit()
            
    user = validate_user(request_data)

    try:
        res = validate_hardware(request_data)
        if isinstance(res, str):
            alternative_request(user[0].get('email'), f"{user[0].get('first_name')} {user[0].get('last_name')}", email_sender, email_username, email_password, res)
            sys.exit()
    except:
        deny_request(request_data, email_sender, email_username, email_password)
        sys.exit()

    json_data = convert_data_to_json(user, request_data, res)
    post_requests(json_data)
    approve_request(request_data, email_sender, email_username, email_password)
    data = fetch_requests()
    export_to_docx(data, "user_requests")
    export_to_xlsx(data, "user_requests")
    sys.exit()


if __name__ == "__main__":
    main()