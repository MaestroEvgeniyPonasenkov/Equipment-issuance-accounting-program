from . import board_class


def creating_boards(hardwares: list[dict]) -> list[board_class.Board]:
    """
    Creates a list of board_class.Board objects from a list of hardware dictionaries.

    Parameters:
    hardwares (list[dict]): A list of dictionaries with hardware information.

    Returns:
    list[board_class.Board]: A list of board_class.Board objects created from the hardware information.
    """
    lst = []
    for board in hardwares:
        name = board.get('name')
        specifications = board.get('specifications')
        log_elems = specifications.get('log_elems')
        memory = specifications.get('memory')
        pll = specifications.get('pll')
        multiplier = specifications.get('multiplier')
        pins = specifications.get('pins')
        board_cls = board_class.Board(
            log_elems, memory, pll, multiplier, pins, name)
        lst.append(board_cls)
    return lst


def find_alternative_board(hardware: dict, hardwares: list[dict]) -> str:
    """
    Finds an alternative board from a list of board_class.Board objects based on a given hardware dictionary.

    Parameters:
    hardware (dict): A dictionary with the hardware information.
    hardwares (list[dict]): A list of dictionaries with hardware information.

    Returns:
    board_class.Board: An alternative board_class.Board object.

    Raises:
    ValueError: If an alternative board cannot be found.
    """
    board = creating_boards([hardware])[0]
    hardwares = creating_boards(hardwares)
    try:
        alternative = board.get_alternative(hardwares)
        return alternative
    except Exception:
        return ""
