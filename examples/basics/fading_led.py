"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/basics/Fade
"""
from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    led: int = 9
    brightness: int = 0
    fade_amount: int = 5

    def setup() -> None:
        pinMode(led, OUTPUT)

    def loop() -> None:
        global brightness, fade_amount

        analogWrite(led, brightness)
        brightness = brightness + fade_amount

        if brightness <= 0 or brightness >= 255:
            fade_amount = -fade_amount

        delay(30)
