import json
from bs4 import BeautifulSoup


def convert_email_to_dict(email_body: str) -> dict:
    """
    Converts email body html to dictionary with key-value pairs.

    Parameters:
    email_body (str): HTML body of email.

    Returns:
    dict: Dictionary containing key-value pairs extracted from email HTML.
    """
    soup = BeautifulSoup(email_body, 'html.parser')
    pre_tag = soup.find('pre')
    raw_data = pre_tag.get_text()
    data = raw_data.strip()
    kv_string = data[:data.find("\n")]
    result = kv_string.split(" , ")
    dictionary = {}
    for item in result:
        key, value = item.split(' ', 1)
        dictionary[key] = value
    dictionary['Плата'] = dictionary['Плата'].split(', ')
    return dictionary


def convert_email_to_json(data: dict) -> str:
    """
    Converts dictionary to JSON string format.

    Parameters:
    data (dict): Dictionary containing key-value pairs.

    Returns:
    str: JSON formatted string.
    """
    request_data = {
        "user": data.get('Имя пользователя'),
        "location": data.get('Расположение'),
        "status": "new",
        "comment": data.get('Комментарий'),
        "taken_date": data.get('Дата взятия'),
        "return_date": data.get('Дата возврата'),
        "issued_by": 0,
        "hardware": [{"hardware": data.get('Название платы'), "count": data.get('Количество')}]
    }
    request_body = json.dumps(request_data, ensure_ascii=False)
    return request_body