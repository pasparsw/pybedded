"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/digital/InputPullupSerial
"""
from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    def setup() -> None:
        Serial.begin(9600)
        pinMode(2, INPUT_PULLUP)
        pinMode(13, OUTPUT)

    def loop() -> None:
        sensor_val: int = digitalRead(2)
        Serial.println(sensor_val)

        if sensor_val == HIGH:
            digitalWrite(13, LOW)
        else:
            digitalWrite(13, HIGH)
