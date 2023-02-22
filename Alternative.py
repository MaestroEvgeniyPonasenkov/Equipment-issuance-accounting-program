import json


class Board:
    def __init__(self, log_elems, memory, pll, multiplier, pins, name):
        self.name = name
        self.log_elems = log_elems
        self.memory = memory
        self.pll = pll
        self.multiplier = multiplier
        self.pins = pins

    def get_alternative(self, board_lst: list) -> str:
        with open("max_variance.json", "r") as file:
            variance = json.load(file)
        points = [0 for _ in board_lst]
        for stat_index, stat in enumerate(list(self.__dict__.items())[1:], 1):
            stat_now = [list(_.__dict__.values())[stat_index] for _ in board_lst]
            best_var = 0
            for st in stat_now:
                if st > best_var:
                    var = stat[1] - st
                    if var <= 0 or var <= variance.get(stat[0])[0]:
                        best_var = st
            if best_var:
                points[stat_now.index(best_var)] += variance.get(stat[0])[1]
        return board_lst[points.index(max(points))].name
