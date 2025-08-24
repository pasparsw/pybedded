from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    CHIP_SELECT: int = 4

    def setup() -> None:
        Serial.begin(9600)
        while not Serial:
            pass

        Serial.print("Initializing SD card...")

        if not SD.begin(CHIP_SELECT):
            Serial.println("Card failed or not present")
            while True:
                pass

        Serial.println("Card initialized.")
        data_file: File = SD.open("datalog.txt")

        if data_file:
            while data_file.available():
                Serial.write(data_file.read())
            data_file.close()
        else:
            Serial.println("error opening datalog.txt")

    def loop() -> None:
        pass
