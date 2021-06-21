from digitalio import Direction
from socd import NeutralCleaner
from io_pad_map import (UP, DOWN, LEFT, RIGHT, A, B, X, Y,
                        RB, LB, RT, LT, START, SELECT)

#     |---|
#     | ^ |
# |---|---|---|
# | < | . | > |
# |---|---|---|

# |-----------------|
# | X | Y | Rb | Rt |
# |-----------------|
# | A | B | Lb | Lt |
# |-----------------|

# |----------------|
# | Start | Select |
# |----------------|


class Gamepad:
    def __init__(self, cleaner=NeutralCleaner):
        self.directions = [UP, DOWN, LEFT, RIGHT]
        self.actions = [A, B, X, Y, RB, LB, RT, LT]
        self.misc = [START, SELECT]
        self.cleaner = cleaner

    def read_directions(self):
        return cleaner.clean({dir.name: dir.read() for dir in self.directions()})

    def read_actions(self):
        return {a.name: a.read() for a in self.actions()}

