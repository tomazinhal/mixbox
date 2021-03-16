from digitalio import Direction
from io_pad_map import (up, down, left, right, a, b, x, y,
                        lt, rt, lb, rb, start, select)


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
    def __init__(self, cleaner=None):
        self.directions = [up, down, left, right]
        self.actions = [a, b, x, y, rb, lb, rt, lt]
        self.misc = [start, select]
        self._init_buttons()
        # TODO: add cleaner. self.cleaner = cleaner

    def _init_buttons(self):
        buttons = self.directions + self.actions + self.misc
        for button in buttons:
            button.direction = Direction.INPUT

    def read_directions(self):
        return {
            'up': up.value,
            'down': down.value,
            'left': left.value,
            'right': right.value
        }.copy()

    def read_actions(self):
        return {
            'a': A.value,
            'b': B.value,
            'x': X.value,
            'y': Y.value,
            'rb': Rb.value,
            'lb': Lb.value,
            'rt': Rt.value,
            'lt': Lt.value,
            'start': start.value,
            'select': select.value
        }.copy()
