from typing import Any


class Serial:
    @staticmethod
    def begin(baudrate: int) -> int:
        pass

    @staticmethod
    def available() -> bool:
        pass

    @staticmethod
    def print(message: Any) -> None:
        pass

    @staticmethod
    def println(message: Any) -> None:
        pass

    @staticmethod
    def read() -> str:
        pass

    @staticmethod
    def write() -> str:
        pass
