from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    port_one: SoftwareSerial = SoftwareSerial(10, 11)
    port_two: SoftwareSerial = SoftwareSerial(8, 9)

    def setup() -> None:
        Serial.begin(9600)
        while not Serial:
            pass

        port_one.begin(9600)
        port_two.begin(9600)

    def loop() -> None:
        port_one.listen()
        Serial.println("Data from port one:")

        while port_one.available():
            in_byte: byte = port_one.read()
            Serial.write(in_byte)

        Serial.println("")

        port_two.listen()
        Serial.println("Data from port two:")

        while port_two.available():
            in_byte: byte = port_two.read()
            Serial.write(in_byte)

        Serial.println("")
