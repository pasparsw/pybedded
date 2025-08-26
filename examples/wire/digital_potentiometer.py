from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    val: byte = 0

    def setup() -> None:
        Wire.begin()

    def loop() -> None:
        global val

        Wire.beginTransmission(44)
        Wire.write(byte(0x00))
        Wire.write(val)
        Wire.endTransmission()

        val += 1

        if val == 64:
            val = 0

        delay(500)
