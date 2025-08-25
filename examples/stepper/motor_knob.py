from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    STEPS: int = 100
    stepper: Stepper = Stepper(STEPS, 8, 9, 10, 11)
    previous: int = 0

    def setup() -> None:
        stepper.setSpeed(30)

    def loop() -> None:
        global previous

        val: int = analogRead(0)
        stepper.step(val - previous)

        previous = val
