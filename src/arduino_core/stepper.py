import logging

LOGGER = logging.getLogger("Stepper")

class Stepper:
    def __init__(self, steps: int, pin_1: int, pin_2: int, pin_3: int, pin_4: int):
        LOGGER.info(f"Initializing stepper with steps {steps} on pins {pin_1}, {pin_2}, {pin_3}, {pin_4}")

        self.__steps: int = steps
        self.__pin_1: int = pin_1
        self.__pin_2: int = pin_2
        self.__pin_3: int = pin_3
        self.__pin_4: int = pin_4

    def setSpeed(self, speed: int) -> None:
        LOGGER.info(f"Setting speed to {speed} on motor attached to {self.__pin_1}, {self.__pin_2}, {self.__pin_3}, "
                    f"{self.__pin_4}")

    def step(self, value: int) -> None:
        LOGGER.info(f"Performing {value} steps on motor attached to {self.__pin_1}, {self.__pin_2}, {self.__pin_3}, "
                    f"{self.__pin_4}")
