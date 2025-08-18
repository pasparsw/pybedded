"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/basics/AnalogReadSerial
"""
from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    def setup() -> None:
        Serial.begin(9600)

    def loop() -> None:
        sensor_value: int = analogRead(A0)
        Serial.println(sensor_value)
        delay(1)
