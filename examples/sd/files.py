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
            Serial.println("initialization failed!")
            while True:
                pass
        Serial.println("initialization done.")

        if SD.exists("example.txt"):
            Serial.println("example.txt exists")
        else:
            Serial.println("example.txt doesn't exists")

        Serial.println("Creating example.txt")
        my_file = SD.open("example.txt", FILE_WRITE)
        my_file.close()

        if SD.exists("example.txt"):
            Serial.println("example.txt exists")
        else:
            Serial.println("example.txt doesn't exists")

        Serial.println("Removing example.txt")
        SD.remove("example.txt")

        if SD.exists("example.txt"):
            Serial.println("example.txt exists")
        else:
            Serial.println("example.txt doesn't exists")

    def loop() -> None:
        pass
