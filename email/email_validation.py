from email_convertation import convert_email_to_dict
import os
from dotenv import load_dotenv
from email_utils import get_mail
import sys
import json
path = os.getcwd()
sys.path.append(path)
from db_api import fetch_user, fetch_hardware, fetch_location, post_user


def validate_location():
    """
    Validates if the given location exists in the database.

    Returns:
        True if the location exists in the database, otherwise raise ValueError
    """
    location = get_data('Аудитория')
    locs = fetch_location()
    chck = any([loc.get('name') == location for loc in locs])
    if chck:
        return True
    else:
        raise ValueError("Аудитория не найдена")


def validate_hardware():
    """
    Validates if the given hardware exists in the database.

    Returns:
        True if the hardware exists in the database, otherwise False
    """
    hardware = get_data('Плата')
    hardwares = fetch_hardware()
    chck = any([hws.get('name') == hardware for hws in hardwares])
    if chck:
        return True
    else:
        #Альтернатива
        pass


def validate_user():
    """
    Validates if the user exists in the database. If not, creates a new user using the given input fields.

    Returns:
        True if the user exists in the database or has been created successfully, otherwise False
    """
    firstname = get_data('Имя')
    lastname = get_data('Фамилия')
    status_code = fetch_user(firstname, lastname)
    if status_code == 200:
        return True
    else:
        email = get_data('Почта')
        phone = get_data('Телефон')
        create_user(firstname, lastname, email, phone)
    


def create_user(fname, lname, email, phone):
    """
    Creates a new user using given input fields.

    Args:
        fname: First name of the user.
        lname: Last name of the user.
        email: Email of the user.
        phone: Phone number of the user.

    Returns:
        None
    """
    user_data = {
        "active": True,
        "type": "user",
        "first_name": fname,
        "last_name": lname,
        "patronymic": "string",
        "image_link": "string",
        "email": email,
        "phone": phone,
        "card_id": "string",
        "card_key": "string",
        "comment": ""
    }
    request_body = json.dumps(user_data, ensure_ascii=False)
    post_user(request_body)


def get_data(key: str) -> dict:
    """
    Gets the value of a given key from the email message body.

    Args:
        key: Key to search for in the email message body.

    Returns:
        Value associated with the given key in the email message body.
    """
    msg = get_mail(email_username, email_password)
    msg_parsed = convert_email_to_dict(msg)
    data = msg_parsed.get(key)
    return data


load_dotenv()
email_username = os.getenv("EMAIL_USERNAME")
email_password = os.getenv("EMAIL_PASSWORD")
