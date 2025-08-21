import logging

from typing import Any
from src.arduino_core.definitions import byte

LOGGER = logging.getLogger("EEPROM")


class EEPROM:
    @staticmethod
    def length() -> int:
        pass

    @staticmethod
    def write(address: int, value: int) -> None:
        LOGGER.info(f"Writing {value} to address {address}")

    @staticmethod
    def get(address: int, placeholder: Any) -> None:
        LOGGER.info(f"Getting value from address {address}")

    @staticmethod
    def put(address: int, placeholder: Any) -> None:
        LOGGER.info(f"Putting value {placeholder} to address {address}")

    @staticmethod
    def read(address: int) -> byte:
        LOGGER.info(f"Reading value from address {address}")

    @staticmethod
    def update(address: int, value: Any) -> None:
        LOGGER.info(f"Updating address {address} to store value {value}")
