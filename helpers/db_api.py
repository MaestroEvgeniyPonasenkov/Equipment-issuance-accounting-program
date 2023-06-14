import requests
from dotenv import load_dotenv
import os


def fetch_location() -> list[dict]:
    """
    GET request to fetch locations from the API.

    Returns:
        list: List of locations.
    """
    response = requests.get(f"{api_url}/location",
                            headers={'Authorization': db_access_token})
    locations = response.json()
    return locations


def fetch_hardware() -> list[dict]:
    """
    GET request to fetch free boards from the API.

    Returns:
        list: List of available boards.
    """
    response = requests.get(f"{api_url}/hardware",
                            headers={'Authorization': db_access_token})
    hardware = response.json()
    return hardware


def fetch_stock() -> list[dict]:
    """
    GET request to fetch all boards from the API.

    Returns:
        list: List of available boards.
    """
    response = requests.get(f"{api_url}/stocks",
                            headers={'Authorization': db_access_token})
    stock = response.json()
    return stock


def fetch_requests() -> list[dict]:
    """
    GET request to fetch all the equipment requests from the API.

    Returns: 
        list: List of all equipment requests.
    """
    response = requests.get(f"{api_url}/request",
                            headers={'Authorization': db_access_token})
    equipment_requests = response.json()
    return equipment_requests


def fetch_user(fname: str, lname: str, type: str = "user"):
    """
    GET request to fetch user from the API.

    Returns:
        list: List with user data.
    """
    response = requests.get(f"{api_url}/user",
                            headers={'Authorization': db_access_token},
                            params={
                                'first_name': fname,
                                'last_name': lname,
                                'type': type
                            }
                            )
    return response


def post_requests(request_body: str) -> bool:
    """
    POST request to submit a new equipment request to the API.

    Args:
        request_body (str): The request body in JSON format containing information about the new request.

    Returns:
        (bool): shows us was request successful or not
    """
    response = requests.post(f"{api_url}/request",
                             headers={'Authorization': db_access_token},
                             data=request_body
                             )
    equipment_response = response.json()
    if response.status_code == 201:
        print(f"Request was successfully added to database!\ndetails:{equipment_response}")
        return True
    else:
        print(f"Request failed!\ndetails:{equipment_response}")
        return False


def post_user(request_body: str) -> dict:
    """
    POST request to submit a new user to the API.

    Args:
        request_body (dict): The request body containing information about the new request.

    Returns:
        dict: The response from the API containing details of the newly-created request.
    """
    response = requests.post(f"{api_url}/user",
                             headers={'Authorization': db_access_token},
                             data=request_body
                             )
    user_response = response.json()
    return user_response


load_dotenv()
api_url = os.getenv("API_URL")
db_access_token = os.getenv("DB_ACCESS_TOKEN")