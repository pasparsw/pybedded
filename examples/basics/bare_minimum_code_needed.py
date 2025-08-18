"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/basics/BareMinimum
"""
from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    def setup() -> None:
        pass

    def loop() -> None:
        pass
