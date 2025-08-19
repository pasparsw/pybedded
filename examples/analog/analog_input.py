"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/analog/AnalogInput
"""
from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    sensor_pin: int = A0
    led_pin: int = 13
    sensor_value: int = 0

    def setup() -> None:
        pinMode(led_pin, OUTPUT)

    def loop() -> None:
        global sensor_value

        sensor_value = analogRead(sensor_pin)
        digitalWrite(led_pin, HIGH)
        delay(sensor_value)

        digitalWrite(led_pin, LOW)
        delay(sensor_value)
