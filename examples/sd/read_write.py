from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    my_file: File = File()

    def setup() -> None:
        global my_file

        Serial.begin(9600)
        while not Serial:
            pass

        Serial.print("Initializing SD card...")

        if not SD.begin(4):
            Serial.println("Initialization failed!")
            while True:
                pass
        Serial.println("Initialization done")

        my_file = SD.open("test.txt", FILE_WRITE)

        if my_file:
            Serial.print("Writing to test.txt")
            my_file.println("testing 1, 2, 3.")

            my_file.close()
            Serial.println("Done")
        else:
            Serial.println("Error opening test.txt")

        my_file = SD.open("test.txt")

        if my_file:
            Serial.println("test.txt:")

            while my_file.available():
                Serial.write(my_file.read())

            my_file.close()
        else:
            Serial.println("Error opening test.txt")

    def loop() -> None:
        pass
