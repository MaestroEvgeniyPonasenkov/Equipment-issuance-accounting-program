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
        dictionary.update({key: value.strip()})
    dictionary.update(
        {'Почта': "@".join(dictionary.get('Почта').split())})
    dictionary.update({'Количество': int(
        dictionary.get('Количество'))})
    return dictionary