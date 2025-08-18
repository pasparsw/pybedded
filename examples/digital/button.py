"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/digital/Button
"""
from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    BUTTON_PIN: int = 2
    LED_PIN: int = 13

    button_state: int = 0

    def setup() -> None:
        pinMode(LED_PIN, OUTPUT)
        pinMode(BUTTON_PIN, INPUT)

    def loop() -> None:
        global button_state

        button_state = digitalRead(BUTTON_PIN)

        if button_state == HIGH:
            digitalWrite(LED_PIN, HIGH)
        else:
            digitalWrite(LED_PIN, LOW)
