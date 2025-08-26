from typing import Any

from src.arduino_core.definitions import byte, char


class Wire:
    @staticmethod
    def begin(address: int) -> None:
        pass

    @staticmethod
    def beginTransmission(address: int) -> None:
        pass

    @staticmethod
    def write(data: Any) -> None:
        pass

    @staticmethod
    def endTransmission() -> byte:
        return 0

    @staticmethod
    def requestFrom(address: byte, size: int) -> None:
        pass

    @staticmethod
    def available() -> bool:
        return True

    @staticmethod
    def read() -> Any:
        return ""

    @staticmethod
    def onReceive(callback) -> None:
        pass

    @staticmethod
    def onRequest(callback) -> None:
        pass
