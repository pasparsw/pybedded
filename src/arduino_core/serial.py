from typing import Any
from src.arduino_core.definitions import byte, HEX, DEC


class Serial:
    @staticmethod
    def begin(baudrate: int) -> int:
        pass

    @staticmethod
    def available() -> bool:
        pass

    @staticmethod
    def print(message: Any, format: int = DEC) -> None:
        pass

    @staticmethod
    def println(message: Any, format: int = DEC) -> None:
        pass

    @staticmethod
    def read() -> byte:
        pass

    @staticmethod
    def write(data: byte) -> None:
        pass

    @staticmethod
    def parseInt() -> int:
        pass

class Serial1(Serial):
    pass

class Serial2(Serial):
    pass
