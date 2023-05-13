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
    info_div = soup.find('div')
    data = {}
    for div in info_div.find_all('div'):
        span = div.find('span')
        if span:
            text = span.text.strip()
            parts = text.split(':')
            if len(parts) == 2:
                key, value = parts[0].strip(), parts[1].strip()
                data[key] = value
    return data


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