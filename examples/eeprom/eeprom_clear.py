from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    def setup() -> None:
        pinMode(13, OUTPUT)

        for i in range(EEPROM.length()):
            EEPROM.write(i, 0)

        digitalWrite(13, HIGH)

    def loop() -> None:
        pass
