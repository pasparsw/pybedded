import logging

from src.arduino_core.definitions import byte, unsigned_int

LOGGER = logging.getLogger("SPI")

SPI_HALF_SPEED: int = 0

class SPI:
    @staticmethod
    def begin() -> None:
        LOGGER.info(f"Beginning SPI communication")

    @staticmethod
    def transfer(data: byte) -> unsigned_int:
        LOGGER.info(f"Transferring data {data}")
        return 0
