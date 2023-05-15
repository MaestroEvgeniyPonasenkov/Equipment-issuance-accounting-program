import os
import sys
import json
path = os.getcwd()
sys.path.append(path)
from alternative.alternative_board_finder import creating_boards, find_alternative_board
from db_api import fetch_user, fetch_hardware, fetch_location, fetch_stock, post_user


def validate_location(request_data: dict) -> bool:
    """
    Validates if the given location exists in the database.

    Returns:
        True if the location exists in the database, otherwise raise ValueError
    """
    location = request_data.get('Аудитория')
    locs = fetch_location()
    chck = any([loc.get('name') == location for loc in locs])
    if chck:
        return True
    else:
        raise ValueError("Аудитория не найдена")


def validate_hardware(request_data: dict):
    """
    Validates if the given hardware exists in the database.

    Returns:
        True if the hardware exists in the database, otherwise False
    """
    hardware_name = request_data.get('Плата')
    quantity = request_data.get('Количество')
    hardwares = fetch_hardware()
    stock = fetch_stock()
    for hw in hardwares:
        if hw.get('name') == hardware_name:
            hw_id = hw.get('id')
            hardware = hw
    for st in stock:
        st_id = st.get('hardware')
        st_count = st.get('count')
        if st_id == hw_id:
            if st_count >= quantity:
                return hardware.get('id'), quantity
            else:
                hws = creating_boards(hardwares)
                try:
                    alternative_board = find_alternative_board(hardware, hws)
                    return alternative_board
                except Exception:
                    raise TypeError("Ошибка")


def validate_user(request_data: dict):
    """
    Validates if the user exists in the database. If not, creates a new user using the given input fields.

    Returns:
        True if the user exists in the database or has been created successfully, otherwise False
    """
    firstname = request_data.get('Имя')
    lastname = request_data.get('Фамилия')
    response = fetch_user(firstname, lastname)
    if response.status_code == 200:
        return response.json()
    else:
        email = request_data.get('Почта')
        phone = request_data.get('Телефон')
        return create_user(firstname, lastname, email, phone)


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
    print("User was added to database")
    return post_user(request_body)