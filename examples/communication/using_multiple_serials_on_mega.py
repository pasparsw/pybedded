"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/communication/MultiSerialMega
"""
from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.MEGA):
    def setup() -> None:
        Serial.begin(9600)
        Serial1.begin(9600)

    def loop() -> None:
        if Serial1.available():
            in_byte: int = Serial1.read()
            Serial1.write(in_byte)

        if Serial.available():
            in_byte: int = Serial.read()
            Serial.write(in_byte)
