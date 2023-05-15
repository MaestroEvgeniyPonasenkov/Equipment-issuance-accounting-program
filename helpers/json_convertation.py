import json


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
        "location": int(request_data.get('Аудитория')),
        "status": "new",
        "comment": request_data.get('Комментарий'),
        "taken_date": request_data.get('Дата_выдачи'),
        "return_date": request_data.get('Дата_возврата'),
        "issued_by": 0,
        "hardware": [
            {
                "hardware": res[0],
                "count": res[1]
            }
        ]
    }
    request_body = json.dumps(user_data, ensure_ascii=False)
    return request_body
