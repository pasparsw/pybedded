"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/basics/BareMinimum
"""
from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    def request_event() -> None:
        Wire.write("hello ")

    def setup() -> None:
        Wire.begin(8)
        Wire.onRequest(request_event)

    def loop() -> None:
        delay(100)
