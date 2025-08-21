import logging

from src.arduino_core.serial import Serial

LOGGER = logging.getLogger("SoftwareSerial")

class SoftwareSerial(Serial):
    def __init__(self, rx: int, tx: int):
        LOGGER.info(f"Creating software serial port on pins ({rx}, {tx})")

        self.__rx: int = rx
        self.__tx: int = tx

    def listen(self) -> None:
        LOGGER.info(f"Listening on software serial port ({self.__rx}, {self.__tx})")
