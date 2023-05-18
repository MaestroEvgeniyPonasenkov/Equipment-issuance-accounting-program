def get_pins(observed: str) -> list[str]:
    variations = {
        '0': ('0', '8'),
        '1': ('1', '2', '4'),
        '2': ('2', '1', '3', '5'),
        '3': ('3', '2', '6'),
        '4': ('4', '1', '5', '7'),
        '5': ('5', '2', '4', '6', '8'),
        '6': ('6', '3', '5', '9'),
        '7': ('7', '4', '8'),
        '8': ('8', '5', '7', '9', '0'),
        '9': ('9', '6', '8')
    }
    lst_res = [variations.get(el) for el in observed]
    for t in lst_res:
        for item in t:
            
    print(lst_res)
            
            

get_pins("24")