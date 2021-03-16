import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.gamepad import Gamepad

import board
import time
from digitalio import DigitalInOut, Direction

DEVICE = "gamepad"

def init(device):
    """Setup device
    
    returns: device
    """
    if device == "gamepad":
        return Gamepad(usb_hid.devices)
    elif device == "keyboard":
        return Keyboard(usb_hid.devices)

def read_gamepad():
    pass

def toggle(led):
    if led.value == True:
        led.value = False
    elif led.value == False:
        led.value = True

if __name__ == "__main__":
    device = init(DEVICE)

    if DEVICE == "keyboard":
        # Type lowercase 'a'. Presses the 'a' key and releases it.
        device.send(Keycode.A)
        # Type capital 'A'. Presses the 'a' key and releases it.
        device.send(Keycode.SHIFT, Keycode.A)
    
    if DEVICE == "gamepad":
        for i in range(100):
            device.click_buttons(1)
        for i in range(20):
            device.move_joysticks(x=2, y=0, z=-20)


    led = DigitalInOut(board.GP25)
    led.direction = Direction.OUTPUT
    led.value = False
    while True:
        toggle(led)
        time.sleep(0.5)
