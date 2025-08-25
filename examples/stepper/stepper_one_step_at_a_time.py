from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    STEPS_PER_REVOLUTION: int = 200
    my_stepper: Stepper = Stepper(STEPS_PER_REVOLUTION, 8, 9, 10, 11)
    step_count: int = 0

    def setup() -> None:
        Serial.begin(9600)

    def loop() -> None:
        global step_count

        my_stepper.step(1)
        Serial.print("steps:")
        Serial.println(step_count)
        step_count += 1
        delay(500)
