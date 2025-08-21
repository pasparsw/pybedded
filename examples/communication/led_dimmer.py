"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/communication/Dimmer
"""
from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    LED_PIN: int = 9

    def setup() -> None:
        Serial.begin(9600)
        pinMode(LED_PIN, OUTPUT)

    def loop() -> None:
        if Serial.available():
            brightness: byte = Serial.read()
            analogWrite(LED_PIN, brightness)
