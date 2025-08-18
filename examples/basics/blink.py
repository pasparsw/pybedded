"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/basics/Blink
"""
from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    def setup() -> None:
        pinMode(LED_BUILTIN, OUTPUT)

    def loop() -> None:
        digitalWrite(LED_BUILTIN, HIGH)
        delay(1000)
        digitalWrite(LED_BUILTIN, LOW)
        delay(1000)
