import logging

from typing import Any, List
from src.arduino_core.definitions import byte

LOGGER = logging.getLogger("LiquidCrystal")


class LiquidCrystal:
    def __init__(self, rs: int, en: int, d4: int, d5: int, d6: int, d7: int):
        LOGGER.info(f"Initializing LCD on pins {rs}, {en}, {d4}, {d5}, {d6}, {d7}")
        self.__id: str = f"{rs}/{en}/{d4}/{d5}/{d6}/{d7}"

    def begin(self, columns: int, rows: int) -> None:
        LOGGER.info(f"Setting number of columns to {columns} and rows to {rows} on LCD {self.__id}")

    def setCursor(self, column: int, row: int) -> None:
        LOGGER.info(f"Setting cursor to position ({column}, {row}) on LCD {self.__id}")

    def print(self, character: Any) -> None:
        LOGGER.info(f"Printing '{character}' on LCD {self.__id}")

    def autoscroll(self) -> None:
        LOGGER.info(f"Enabling automatic scrolling on LCD {self.__id}")

    def noAutoscroll(self) -> None:
        LOGGER.info(f"Disabling automatic scrolling on LCD {self.__id}")

    def clear(self) -> None:
        LOGGER.info(f"Clearing LCD {self.__id}")

    def noBlink(self) -> None:
        LOGGER.info(f"Disabling cursor blinking on LCD {self.__id}")

    def blink(self) -> None:
        LOGGER.info(f"Enabling cursor blinking on LCD {self.__id}")

    def noCursor(self) -> None:
        LOGGER.info(f"Disabling cursor on LCD {self.__id}")

    def cursor(self) -> None:
        LOGGER.info(f"Enabling cursor on LCD {self.__id}")

    def createChar(self, id: int, character: List[byte]) -> None:
        LOGGER.info(f"Creating new character with ID {id} on LCD {self.__id}: {character}")

    def write(self, id: Any) -> None:
        LOGGER.info(f"Writing character {id} on LCD {self.__id}")

    def noDisplay(self) -> None:
        LOGGER.info(f"Disabling LCD {self.__id}")

    def display(self) -> None:
        LOGGER.info(f"Enabling LCD {self.__id}")

    def scrollDisplayLeft(self) -> None:
        LOGGER.info(f"Scrolling left on LCD {self.__id}")

    def scrollDisplayRight(self) -> None:
        LOGGER.info(f"Scrolling right on LCD {self.__id}")

    def rightToLeft(self) -> None:
        LOGGER.info(f"Setting text direction from right to left on LCD {self.__id}")

    def leftToRight(self) -> None:
        LOGGER.info(f"Setting text direction from left to right on LCD {self.__id}")

    def home(self) -> None:
        LOGGER.info(f"Home LCD {self.__id}")
