import logging

CARD_LOGGER = logging.getLogger("Sd2Card")
VOLUME_LOGGER = logging.getLogger("SdVolume")
FILE_LOGGER = logging.getLogger("SdFile")

SD_CARD_TYPE_SD1: int = 0
SD_CARD_TYPE_SD2: int = 1
SD_CARD_TYPE_SDHC: int = 2

LS_R: int = 0
LS_DATE: int = 1
LS_SIZE: int = 2

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
        FILE_LOGGER.info(f"Opening root of {volume}")

    def ls(self, flags: int) -> None:
        FILE_LOGGER.info(f"Listing files")
