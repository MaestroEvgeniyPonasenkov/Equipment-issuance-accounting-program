from email_utils import get_mail
import os
from dotenv import load_dotenv
from email_convertation import convert_email_to_dict, convert_email_to_json
import sys
path = os.getcwd()
sys.path.append(path)
from db_api import post_requests


def email_hardware_request(email_username: str, email_password: str) -> dict:
    """
    This function accepts email credentials as parameters and retrieves emails from the account.
    It then converts the emails into dictionary objects, then to JSON and finally posts them to a database using API requests.
    
    Parameters:
    email_username (str): Username of the email account.
    email_password (str): Password of the email account.
    
    Returns:
    response (dict): JSON response from the database API.
    """
    message = get_mail(email_username, email_password)
    parsed_message = convert_email_to_dict(message)
    hardware_request = convert_email_to_json(parsed_message)
    response = post_requests(hardware_request)
    return response


load_dotenv()
email_username = os.getenv("EMAIL_USERNAME")
email_password = os.getenv("EMAIL_PASSWORD")
print(email_hardware_request(email_username, email_password))
