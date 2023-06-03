import requests
import json

DB_ACCESS_TOKEN = "Basic NVJOWUJkTGR1VER4UUNjTThZWXJiNW5BOkg0ZFNjQXlHYlM4OUtnTGdaQnMydlBzaw=="
DB_URL = "https://helow19274.ru/aip/api"


def patch_request(table_name: str, col_name: str, value, id: int) -> list[dict]:
    """

    :param table_name: Название таблицы для patch запроса
    :param col_name: Название столбца, который меняется
    :param value: Новое значение
    :param id: ID изменяемоц записи
    :return:
    """
    data = {col_name: value}
    data_json = json.dumps(data, ensure_ascii=False)
    response = requests.patch(f"{DB_URL}/{table_name}/{id}",
                              headers={
                                  'Authorization': DB_ACCESS_TOKEN,
                              },
                              data=data_json
                              ).json()
    return response


def post_request(table_name: str, data: dict) -> dict:
    """

    Args:
        table_name (str): Название таблицы для post запроса
        request_body (dict): The request body containing information about the new request.

    Returns:
        dict: The response from the API containing details of the newly-created request.
    """
    data_json = json.dumps(data, ensure_ascii=False)
    response = requests.post(f"{DB_URL}/{table_name}",
                             headers={'Authorization': DB_ACCESS_TOKEN},
                             data=data_json
                             ).json()
    return response

def get_request(table_name: str) -> list[dict]:
    response = requests.get(f"{DB_URL}/{table_name}",
                            headers={'Authorization': DB_ACCESS_TOKEN}).json()
    return response