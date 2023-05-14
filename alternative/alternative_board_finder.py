from . import board_class


def creating_boards(hardwares: list[dict]) -> list[board_class.Board]:
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


def find_alternative_board(hardware: dict, hardwares: list[board_class.Board]):
    name = hardware.get('name')
    log_elems = hardware.get('log_elems')
    memory = hardware.get('memory')
    pll = hardware.get('pll')
    multiplier = hardware.get('multiplier')
    pins = hardware.get('pins')
    board_cls = board_class.Board(
        log_elems, memory, pll, multiplier, pins, name)
    try:
        alternative = board_cls.get_alternative(hardwares)
        return alternative
    except:
        raise ValueError(
            "Альтернативная плата не найдена!")
