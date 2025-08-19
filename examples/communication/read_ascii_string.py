"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/communication/ReadASCIIString
"""
from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    RED_PIN: int = 3
    GREEN_PIN: int = 5
    BLUE_PIN: int = 6

    def setup() -> None:
        Serial.begin(9600)

        pinMode(RED_PIN, OUTPUT)
        pinMode(GREEN_PIN, OUTPUT)
        pinMode(BLUE_PIN, OUTPUT)

    def loop() -> None:
        while Serial.available():
            red: int = Serial.parseInt()
            green: int = Serial.parseInt()
            blue: int = Serial.parseInt()

            if Serial.read() == '\n':
                red = 255 - constrain(red, 0, 255)
                green = 255 - constrain(green, 0, 255)
                blue = 255 - constrain(blue, 0, 255)

                analogWrite(RED_PIN, red)
                analogWrite(GREEN_PIN, green)
                analogWrite(BLUE_PIN, blue)

                Serial.print(red, HEX)
                Serial.print(green, HEX)
                Serial.println(blue, HEX)
