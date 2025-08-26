from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    def setup() -> None:
        Serial.begin(9600)
        Keyboard.begin()

    def loop() -> None:
        if Serial.available():
            in_char: char = Serial.read()
            Keyboard.write(in_char + 1)
