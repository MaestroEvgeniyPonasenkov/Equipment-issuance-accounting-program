import requests
from dotenv import load_dotenv
import os


def fetch_hardware() -> list:
    """
    GET request to fetch free boards from the API.

    Returns:
        list: List of available boards.
    """
    response = requests.get(f"{api_url}/hardware",
                            headers={'Authorization': db_access_token})
    hardware = response.json()
    return hardware


def fetch_requests() -> list:
    """
    GET request to fetch all the equipment requests from the API.

    Returns: 
        list: List of all equipment requests.
    """
    response = requests.get(f"{api_url}/request",
                            headers={'Authorization': db_access_token})
    equipment_requests = response.json()
    return equipment_requests


def post_requests(request_body: dict) -> dict:
    """
    POST request to submit a new equipment request to the API.

    Args:
        request_body (dict): The request body containing information about the new request.

    Returns:
        dict: The response from the API containing details of the newly-created request.
    """
    response = requests.post(
        f"{api_url}/request", headers={'Authorization': db_access_token}, json=request_body)
    equipment_response = response.json()
    return equipment_response


load_dotenv()
api_url = os.getenv("API_URL")
db_access_token = os.getenv("DB_ACCESS_TOKEN")
request_body = {
    "user": 0,
    "location": 0,
    "status": "new",
    "comment": "",
    "taken_date": "2023-05-13T13:21:30.718Z",
    "return_date": "2023-05-13T13:21:30.718Z",
    "issued_by": 0,
    "hardware": [
        {
            "hardware": 0,
            "count": 0
        }
    ]
}
print(post_requests(request_body))
