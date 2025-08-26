from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    def setup() -> None:
        Ethernet.init(10)
        Serial.begin(9600)

    def loop() -> None:
        link: int = Ethernet.linkStatus()
        Serial.print("Link status: ")

        if link == Unknown:
            Serial.println("Unknown")
        elif link == LinkON:
            Serial.println("ON")
        elif link == LinkOFF:
            Serial.println("OFF")

        delay(1000)
