from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    def receive_event(how_many: int) -> None:
        while Wire.available():
            c: char = Wire.read()
            Serial.print(c)

        x: int = Wire.read()
        Serial.println(x)

    def setup() -> None:
        Wire.begin(8)
        Wire.onReceive(receive_event)
        Serial.begin(9600)

    def loop() -> None:
        delay(100)
