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
    def read() -> Any:
        LOGGER.info(f"Reading byte from serial")
        return 0

    @staticmethod
    def write(data: byte) -> None:
        LOGGER.info(f"Writing seria data {data}")

    @staticmethod
    def parseInt() -> int:
        LOGGER.info(f"Parsing int from serial")
        return 0
    
    @staticmethod
    def availableForWrite() -> int:
        return 0
    
    @staticmethod
    def end() -> None:
        pass

    @staticmethod
    def find(target: str) -> int:
        return 0
    
    @staticmethod
    def findUntil(target: str, terminator: str) -> int:
        return 0
    
    @staticmethod
    def flush() -> None:
        pass

    @staticmethod
    def parseFloat() -> float:
        return 0.0
    
    @staticmethod
    def peek() -> int:
        return 0
    
    @staticmethod
    def readBytes(buffer: bytearray, length: int) -> int:
        return 0
    
    @staticmethod
    def readBytesUntil(terminator: str, buffer: bytearray, length: int) -> int:
        return 0
    
    @staticmethod
    def readString() -> str:
        return ""
    
    @staticmethod
    def readStringUntil(terminator: str) -> str:
        return ""
    
    @staticmethod
    def setTimeout(timeout: int) -> None:
        pass

    @staticmethod
    def serialEvent() -> None:
        pass

class Serial1(Serial):
    pass

class Serial2(Serial):
    pass

class String:
    def __init__(self, value: Any):
        pass

    def __str__(self):
        return ""
