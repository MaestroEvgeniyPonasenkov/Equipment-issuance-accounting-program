import os
import json


def change_var(stat: str, val: int) -> None:
    """
    Changes the value of a specific key in the "max_variance.json" file.

    Parameters:
        stat (str): The name of the key to be updated.
        val (int): The new value for the key.

    Raises:
        TypeError: If the data type of the new value does not match the data type of the old value.
        KeyError: If the key does not exist in the JSON file.
        Exception: If an error occurs during the operation.

    Returns:
        None.
    """
    with open(f"{os.getcwd()}\\alternative\\max_variance.json", "r") as file:
        data = json.load(file)
    try:
        if isinstance(val, type(data.get(stat)[0])):
            data[stat][0] = val
            with open(f"{os.getcwd()}\\alternative\\max_variance.json", 'w') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        else:
            raise TypeError(
                "The data type of the new value does not match the data type of the old value")
    except KeyError:
        print("This parameter does not exist")
    except Exception as e:
        print(f"An error occurred: {str(e)}")