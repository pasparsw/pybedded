"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/communication/PhysicalPixel
"""
from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    incoming_byte: int = 0

    def setup() -> None:
        Serial.begin(9600)
        pinMode(LED_BUILTIN, OUTPUT)

    def loop() -> None:
        global incoming_byte

        if Serial.available():
            incoming_byte = Serial.read()

            if incoming_byte == 'H':
                digitalWrite(LED_BUILTIN, HIGH)
            if incoming_byte == 'L':
                digitalWrite(LED_BUILTIN, LOW)
