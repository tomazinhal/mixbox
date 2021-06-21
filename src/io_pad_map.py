import board
from digitalio import DigitalInOut, Direction

class Button:
    def __init__(self, name: str, pin: DigitalInOut, gamepad_id: int):
        self.name = name
        self.id = gamepad_id
        self.pin = DigitalInOut(pin)
        # set pin as input
        self.pin.direction = Direction.INPUT

    def read(self):
        return pin.value

    def __repr__(self):
        print(f"Button {self.name} on {self.pin} is bound to action {self.id}")

A = Button('a', board.GP14, 1)
B = Button('b', board.GP15, 2)
X = Button('x', board.GP16, 3)
Y = Button('y', board.GP17, 4)
RB = Button('right bumper', board.GP18, 5)
LB = Button('left bumper', board.GP19, 6)
RT = Button('right trigger', board.GP20, 7)
LT = Button('left trigger', board.GP21, 8)
START = Button('start', board.GP22, 9)
SELECT = Button('select', board.GP23, 10)
UP = Button('up', board.GP10, 11)
DOWN = Button('down', board.GP11, 12)
LEFT = Button('left', board.GP12, 13)
RIGHT = Button('right', board.GP13, 14)

