from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    my_serial: SoftwareSerial = SoftwareSerial(10, 11)

    def setup() -> None:
        Serial.begin(57600)
        while not Serial:
            pass

        Serial.println("Goodnight moon!")

        my_serial.begin(4800)
        my_serial.println("Hello, world?")

    def loop() -> None:
        if my_serial.available():
            Serial.write(my_serial.read())
        if Serial.available():
            my_serial.write(Serial.read())
