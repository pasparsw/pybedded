"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/basics/BareMinimum
"""
from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    x: byte = 0

    def setup() -> None:
        Wire.begin()

    def loop() -> None:
        global x

        Wire.beginTransmission(8)
        Wire.write("x is ")
        Wire.write(x)
        Wire.endTransmission()

        x += 1
        delay(500)
