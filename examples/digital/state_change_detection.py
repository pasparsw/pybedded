"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/digital/StateChangeDetection
"""
from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    BUTTON_PIN: int = 2
    LED_PIN: int = 13

    button_push_counter: int = 0
    button_state: int = 0
    last_button_state: int = 0

    def setup() -> None:
        pinMode(BUTTON_PIN, INPUT)
        pinMode(LED_PIN, OUTPUT)
        Serial.begin(9600)

    def loop() -> None:
        global button_state, button_push_counter, last_button_state

        button_state = digitalRead(BUTTON_PIN)

        if button_state != last_button_state:
            if button_state == HIGH:
                button_push_counter += 1

                Serial.println("on")
                Serial.print("number of button pushes: ")
                Serial.println(button_push_counter)
            else:
                Serial.println("off")

            delay(50)

        last_button_state = button_state
