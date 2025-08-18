"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/basics/DigitalReadSerial
"""
from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    push_button: int = 2

    def setup() -> None:
        Serial.begin(9600)
        pinMode(push_button, INPUT)

    def loop() -> None:
        button_state: int = digitalRead(push_button)
        Serial.println(button_state)
        delay(1)
