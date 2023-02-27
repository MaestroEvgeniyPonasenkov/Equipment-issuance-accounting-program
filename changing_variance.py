import json


def change_var(stat: str, val: int) -> None:
    """Changing the file with the maximum variance of characteristics of the boards"""

    with open("max_variance.json", "w") as file:
        data = json.load(file)
    try:
        if type(val) == type(data.get(stat)):
            data[stat][0] = val
        with open('myfile.json', 'w') as f:
            json.dump(data, ensure_ascii=False, indent=4)
    except Exception:
        print("This parameter does not exist")
