import json
import datetime


def add_time_to_date(date: str) -> str:
    """
    Takes a string representing a date in the format YYYY-MM-DD and returns a string representing
    the same date and time at which the function is called in ISO format.

    Args:
    - date: A string representing a date in the format YYYY-MM-DD.

    Returns:
    - formatted_datetime: A string representing the date and time at which the function is called
                        in ISO format (YYYY-MM-DDTHH:MM:SS.sssZ).
    """
    now = datetime.datetime.now()
    date_lst = [int(_) for _ in date.split('-')]
    year = date_lst[0]
    month = date_lst[1]
    day = date_lst[2]
    new_date = datetime.datetime(
        year, month, day, now.hour, now.minute, now.second, now.microsecond)
    formatted_datetime = new_date.isoformat()
    return formatted_datetime


def convert_data_to_json(user: dict, request_data: dict, res: tuple[int]) -> str:
    """
    Given a Python object, this function converts it to a JSON format.

    Args:
        data: Python object that needs to be converted.

    Returns:
        A JSON formatted Python object.
    """
    user_data = {
        "user": user.get('id'),
        "location": request_data.get('Аудитория'),
        "status": "new",
        "comment": request_data.get('Комментарий'),
        "taken_date": add_time_to_date(request_data.get('Дата_выдачи')),
        "return_date": add_time_to_date(request_data.get('Дата_возврата')),
        "issued_by": 2,
        "hardware": [
            {
                "hardware": res[0],
                "count": res[1]
            }
        ]
    }
    request_body = json.dumps(user_data, ensure_ascii=False)
    return request_body