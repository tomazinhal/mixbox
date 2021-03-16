import board
import time
from digitalio import DigitalInOut, Direction
import socd
import directions as dir

def toggle(led):
    if led.value == True:
        led.value = False
    elif led.value == False:
        led.value = True

if __name__ == "__main__":
    led = DigitalInOut(board.GP25)
    led.direction = Direction.OUTPUT
    led.value = False
    for i in range(10):
        toggle(led)
        time.sleep(0.1)
    print("Booted")
