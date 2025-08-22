from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    SLAVE_SELECT_PIN: int = 10

    def digital_pot_write(address: int, value: int) -> None:
        digitalWrite(SLAVE_SELECT_PIN, LOW)
        delay(100)

        SPI.transfer(address)
        SPI.transfer(value)

        delay(100)

        digitalWrite(SLAVE_SELECT_PIN, HIGH)

    def setup() -> None:
        pinMode(SLAVE_SELECT_PIN, OUTPUT)
        SPI.begin()

    def loop() -> None:
        for channel in range(6):
            for level in range(255):
                digital_pot_write(channel, level)
                delay(10)

            delay(100)

            for level in range(255):
                digital_pot_write(channel, 255 - level)
                delay(10)
