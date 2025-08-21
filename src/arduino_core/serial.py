import logging

from typing import Any
from src.arduino_core.definitions import byte, DEC

LOGGER = logging.getLogger("Serial")


class Serial:
    @staticmethod
    def begin(baudrate: int) -> None:
        LOGGER.info(f"Starting serial communication with baudrate {baudrate}")

    @staticmethod
    def available() -> bool:
        LOGGER.info(f"Checking if any data is available on serial")
        return True

    @staticmethod
    def print(message: Any, format: int = DEC) -> None:
        LOGGER.info(f"Printing '{message}' in {format} format")

    @staticmethod
    def println(message: Any, format: int = DEC) -> None:
        LOGGER.info(f"Printing new line '{message}' in {format} format")

    @staticmethod
    def read() -> byte:
        LOGGER.info(f"Reading byte from serial")
        return 0

    @staticmethod
    def write(data: byte) -> None:
        LOGGER.info(f"Writing seria data {data}")

    @staticmethod
    def parseInt() -> int:
        LOGGER.info(f"Parsing int from serial")
        return 0

class Serial1(Serial):
    pass

class Serial2(Serial):
    pass

class String:
    def __init__(self, value: Any):
        pass

    def __str__(self):
        return ""
