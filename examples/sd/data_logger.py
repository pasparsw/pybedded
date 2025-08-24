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

        Serial.println("card initialized.")

    def loop() -> None:
        data_string: str = ""

        for analog_pin in range(3):
            sensor: int = analogRead(analog_pin)
            data_string += str(sensor)

            if analog_pin < 2:
                data_string += ","

        data_file: File = SD.open("datalog.txt", FILE_WRITE)

        if data_file:
            data_file.println(data_string)
            data_file.close()

            Serial.println(data_string)
        else:
            Serial.println("Error opening dialog.txt")
