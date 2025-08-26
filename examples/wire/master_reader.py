from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    def setup() -> None:
        Wire.begin()
        Serial.begin(9600)

    def loop() -> None:
        Wire.requestFrom(8, 6)

        while Wire.available():
            c: char = Wire.read()
            Serial.print(c)

        delay(500)
