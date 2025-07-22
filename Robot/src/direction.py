from enum import Enum

class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

    def __init__(self, delta_row, delta_col):
        self.delta_row = delta_row
        self.delta_col = delta_col
