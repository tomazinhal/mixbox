from socd import NeutralCleaner


UP = {
    'up': True,
    'down': False,
    'left': False,
    'right': False
}

UP_DOWN = {
    'up': True,
    'down': True,
    'left': False,
    'right': False
}

DOWN = {
    'up': False,
    'down': True,
    'left': False,
    'right': False
}

LEFT = {
    'up': False,
    'down': False,
    'left': True,
    'right': False
}

LEFT_RIGHT = {
    'up': False,
    'down': False,
    'left': True,
    'right': True
}

RIGHT = {
    'up': False,
    'down': False,
    'left': False,
    'right': True
}

NEUTRAL = {
    'up': False,
    'down': False,
    'left': False,
    'right': False
}

def directions_up_down():
    directions = [UP, UP_DOWN, DOWN]
    for direction in directions.copy():
        yield direction

def directions_left_right():
    directions = [LEFT, LEFT_RIGHT, RIGHT]
    for direction in directions.copy():
        yield direction

class Mockpad:
    def __init__(self):
        pass

