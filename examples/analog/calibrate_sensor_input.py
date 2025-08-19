"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/analog/Calibration
"""
from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    SENSOR_PIN: int = A0
    LED_PIN: int = 9

    sensor_value: int = 0
    sensor_min: int = 1023
    sensor_max: int = 0

    def setup() -> None:
        global sensor_value, sensor_max, sensor_min

        pinMode(13, OUTPUT)
        digitalWrite(13, HIGH)

        while millis() < 5000:
            sensor_value = analogRead(SENSOR_PIN)

            if sensor_value > sensor_max:
                sensor_max = sensor_value
            if sensor_value < sensor_min:
                sensor_min = sensor_value

        digitalWrite(13, LOW)

    def loop() -> None:
        global sensor_value

        sensor_value = analogRead(SENSOR_PIN)
        sensor_value = constrain(sensor_value, sensor_min, sensor_max)
        sensor_value = map(sensor_value, sensor_min, sensor_max, 0, 255)

        analogWrite(LED_PIN, sensor_value)
