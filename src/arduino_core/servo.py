import logging

LOGGER = logging.getLogger("Servo")

class Servo:
    def __init__(self):
        self.__pin: int = -1

    def attach(self, pin: int) -> None:
        LOGGER.info(f"Attaching servo on pin {pin}")
        self.__pin = pin

    def write(self, value: int) -> None:
        if self.__pin == -1:
            raise RuntimeError(f"Can't write servo position before attaching it to the pin!")

        LOGGER.info(f"Setting servo on pin {self.__pin} to {value} degrees")

    def read(self) -> int:
        if self.__pin == -1:
            raise RuntimeError(f"Can't read servo position before attaching it to the pin!")

        LOGGER.info(f"Reading position of the servo on pin {self.__pin}")
        return 0
