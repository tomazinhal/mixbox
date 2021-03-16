import board
from digitalio import DigitalInOut, Direction

class Button:
    def __init__(self, name: str, pin: DigitalInOut, gamepad_id: int):
        self.name = name
        self.id = gamepad_id
        self.pin = DigitalInOut(pin)
        # set pin as input
        self.pin.direction = Direction.INPUT

    def __repr__(self):
        print(f"Button {self.name} on {self.pin} is bound to action {self.id}")

up = DigitalInOut(board.GP10)
down = DigitalInOut(board.GP11)
left = DigitalInOut(board.GP12)
right = DigitalInOut(board.GP13)
a = DigitalInOut(board.GP14)
b = DigitalInOut(board.GP15)
x = DigitalInOut(board.GP16)
y = DigitalInOut(board.GP17)
rb = DigitalInOut(board.GP18)
lb = DigitalInOut(board.GP19)
rt = DigitalInOut(board.GP20)
lt = DigitalInOut(board.GP21)
start = DigitalInOut(board.GP22)
select = DigitalInOut(board.GP23)

UP = board.GP10
DOWN = board.GP11
LEFT = oard.GP12
RIGHT = board.GP13

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
