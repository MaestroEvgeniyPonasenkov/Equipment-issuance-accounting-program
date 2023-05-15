import json
import os


class Board:
    def __init__(self, log_elems: int, memory: int, pll: int, multiplier: int, pins: int, name: str) -> None:
        self.name = name
        self.log_elems = log_elems
        self.memory = memory
        self.pll = pll
        self.multiplier = multiplier
        self.pins = pins

    def get_alternative(self, board_lst: list['Board']) -> str:
        """
        This method takes a list of Board objects as a parameter.
        It then loads data from a JSON file named 'max_variance.json' which contains maximum variance.
        The method then compares the characteristics of all available boards with the characteristics of the current Board object.
        Based on the differences from the values in 'max_variance.json', it calculates a score for each board.
        Finally, the method returns the name of the board with the highest score.

        Parameters:
            board_lst (list): A list of Board objects for which we need to find the alternative.

        Returns:
            str: The name of the board with the highest score.
        """
        try:
            with open(f"{os.getcwd()}\\alternative\\max_variance.json", "r") as file:
                variance = json.load(file)
            points = [0 for _ in board_lst]
            for stat_index, stat in enumerate(list(self.__dict__.items())[1:], 1):
                stat_now = [list(_.__dict__.values())[stat_index]
                            for _ in board_lst]
                best_var = 0
                for st in stat_now:
                    if st > best_var:
                        var = stat[1] - st
                        if var <= 0 or var <= variance.get(stat[0])[0]:
                            best_var = st
                if best_var:
                    points[stat_now.index(
                        best_var)] += variance.get(stat[0])[1]
            if best_var == 0:
                raise ValueError(
                    "Альтернативная плата не найдена!")
            return board_lst[points.index(max(points))].name
        except:
            raise ValueError(
                "Альтернативная плата не найдена!")
