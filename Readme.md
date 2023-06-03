**ReadMe**

This is a Python program for handling user requests. It requires environmental variables to run which are loaded using the `dotenv` package.

### Requirements

To use this program, you need to have the following installed:

1. Python 3
2. pip
3. Packages specified in `requirements.txt`

### Installation

1. Clone the repository - `git clone <repository url>`
2. Install dependencies - `pip install -r requirements.txt`
3. Rename the `.env.example` file to `.env` and fill in the environment variables according to your email server requirements (e.g. EMAIL_SENDER, EMAIL_USERNAME, EMAIL_PASSWORD).
4. Run the script - `python main.py`.

### How it works

The program checks a specific mailbox for new user requests, converts the requests to a dictionary and validates the user's information. If everything checks out, the program saves the new user's information to a database, approves the request and exports all user requests to an excel file and a word document. If any errors occur during validation or the user request does not meet certain requirements (e.g. correct hardware), the program sends a denial email to the user with the appropriate reason for their request being denied.

### Usage

1. Make sure the environmental variables are correctly set and the email account has new user requests.
2. Run the script - `python main.py`
3. The program will automatically validate the user requests and email users the result if the request is denied. If approved, the request will be saved to a database and the data will be exported to excel and word documents named "user_requests".

   https://forms.yandex.ru/cloud/64600b76c769f185157c6e64/
