import json
from . import db_api
from alternative.alternative_board_finder import find_alternative_board


def validate_location(request_data: dict) -> bool:
    """
    Validates if the given location exists in the database.

    Returns:
        True if the location exists in the database, otherwise raise ValueError
    """
    location = request_data.get('Аудитория')
    locs = db_api.fetch_location()
    check = False
    location_id = None
    for loc in locs:
        if location == loc.get('name'):
            check = True
            location_id = loc.get('id')
    if check:
        return location_id
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
    try:
        availability = check_availability(hardware_name, quantity)
    except TypeError:
        raise TypeError("Не найдена плата с таким названием!")
    hardwares, hardware, hardware_id, available = availability
    if available:
        return hardware_id, quantity
    else:
        alternative_board_name = find_alternative_board(hardware, hardwares)
        if alternative_board_name:
            alternative_availability = check_availability(alternative_board_name, quantity)
            alternative_available = alternative_availability[3]
            if alternative_available:
                return alternative_board_name
            else:
                raise TypeError("Не найдено альтернативных плат!")
        else:
            raise TypeError("Не найдено альтернативных плат!")


def validate_user(request_data: dict) -> dict:
    """
    Validates if the user exists in the database. If not, creates a new user using the given input fields.

    Returns:
        True if the user exists in the database or has been created successfully, otherwise False
    """
    firstname = request_data.get('Имя')
    lastname = request_data.get('Фамилия')
    response = db_api.fetch_user(firstname, lastname)
    if response.status_code == 200:
        try:
            return response.json()[0]
        except IndexError:
            return {}
    else:
        email = request_data.get('Почта')
        phone = request_data.get('Телефон')
        patronymic = request_data.get('Отчество')
        return create_user(firstname, lastname, patronymic, email, phone)


def create_user(fname: str, lname: str, patronymic: str, email: str, phone: str) -> dict:
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
        "patronymic": patronymic,
        "image_link": "string",
        "email": email,
        "phone": phone,
        "card_id": "string",
        "card_key": "string",
        "comment": ""
    }
    request_body = json.dumps(user_data, ensure_ascii=False)
    print("User was added to database")
    return db_api.post_user(request_body)


def check_availability(hardware_name: str, quantity: int) -> tuple:
    """
    Check if the given hardware is available in the database and returns a tuple.

    Args:
        hardware_name: Name of the hardware.
        quantity: Required quantity of the hardware.

    Returns:
        A tuple with 4 values:
            - list: List of all hardwares in the database.
            - dict: Specific hardware being searched for.
            - int: id of the specific hardware.
            - bool: Boolean value indicating if the required hardware is available in the required quantity or not.
    """
    hardwares = db_api.fetch_hardware()
    stock = db_api.fetch_stock()
    hw_id = None
    hardware = None
    for hw in hardwares:
        if hw.get('name') == hardware_name:
            hw_id = hw.get('id')
            hardware = hw
    if hw_id is None:
        raise TypeError("Ошибка")
    if any([st.get('hardware') == hw_id for st in stock]):
        raise TypeError("Ошибка")
    for st in stock:
        st_id = st.get('hardware')
        st_count = st.get('count')
        if st_id == hw_id:
            if st_count >= quantity:
                return hardwares, hardware, hw_id, True
            else:
                return hardwares, hardware, hw_id, False
