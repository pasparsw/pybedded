"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/analog/AnalogWriteMega
"""
from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.MEGA):
    LOWEST_PIN: int = 2
    HIGHEST_PIN: int = 13

    def setup() -> None:
        for this_pin in range(LOWEST_PIN, HIGHEST_PIN):
            pinMode(this_pin, OUTPUT)

    def loop() -> None:
        for this_pin in range(LOWEST_PIN, HIGHEST_PIN):
            for brightness in range(255):
                analogWrite(this_pin, brightness)
                delay(2)

            for brightness in range(255, 0, -1):
                analogWrite(this_pin, brightness)
                delay(2)

            delay(100)
