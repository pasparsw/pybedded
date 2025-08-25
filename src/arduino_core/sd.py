import logging

from typing import Any
from src.arduino_core.definitions import byte

FILE_LOGGER = logging.getLogger("File")
SD_LOGGER = logging.getLogger("SD")
CARD_LOGGER = logging.getLogger("Sd2Card")
VOLUME_LOGGER = logging.getLogger("SdVolume")
SD_FILE_LOGGER = logging.getLogger("SdFile")

SD_CARD_TYPE_SD1: int = 0
SD_CARD_TYPE_SD2: int = 1
SD_CARD_TYPE_SDHC: int = 2

LS_R: int = 0
LS_DATE: int = 1
LS_SIZE: int = 2

FILE_READ: int = 0
FILE_WRITE: int = 1

class File:
    def print(self, data: Any) -> None:
        FILE_LOGGER.info(f"Printing {data}")

    def println(self, data: Any) -> None:
        FILE_LOGGER.info(f"Printing new line {data}")

    def close(self) -> None:
        FILE_LOGGER.info(f"Closing")

    def read(self) -> byte:
        FILE_LOGGER.info("Reading")
        return ""

    def available(self) -> bool:
        FILE_LOGGER.info(f"Checking if available")
        return True

    def openNextFile(self) -> "File":
        FILE_LOGGER.info(f"Opening next file")
        return File()

    def name(self) -> str:
        return ""

    def isDirectory(self) -> bool:
        return True

    def size(self) -> int:
        return 0

    def availableForWrite(self) -> bool:
        return True

    def write(self, data: Any, size: int) -> None:
        FILE_LOGGER.info(f"Writing to file data of size {size}: {data}")

class SD:
    @staticmethod
    def begin(pin: int) -> bool:
        SD_LOGGER.info(f"Beginning SD communication on chip select pin {pin}")
        return True

    @staticmethod
    def open(path: Any, operation: int = FILE_READ) -> File:
        SD_LOGGER.info(f"Opening file {path} ({operation})")
        return File()

    @staticmethod
    def exists(path: str) -> bool:
        SD_LOGGER.info(f"Checking if {path} exists")
        return True

    @staticmethod
    def remove(path: str) -> None:
        SD_LOGGER.info(f"Removing {path}")

class Sd2Card:
    def init(self, spi_speed: int, chip_select: int) -> bool:
        CARD_LOGGER.info(f"Initializing SD card with SPI speed {spi_speed} and chip select pin {chip_select}")
        return True

    def type(self) -> int:
        return 0

class SdVolume:
    def init(self, card: Sd2Card) -> bool:
        VOLUME_LOGGER.info(f"Initializing volume with card {card}")
        return True

    def clusterCount(self) -> int:
        VOLUME_LOGGER.info(f"Getting volume's cluster count")
        return 0

    def blocksPerCluster(self) -> int:
        VOLUME_LOGGER.info(f"Getting volume's blocks per cluster")
        return 0

    def fatType(self) -> int:
        VOLUME_LOGGER.info(f"Getting volume's FAT type")
        return 0

class SdFile:
    def openRoot(self, volume: SdVolume) -> None:
        SD_FILE_LOGGER.info(f"Opening root of {volume}")

    def ls(self, flags: int) -> None:
        SD_FILE_LOGGER.info(f"Listing files")
