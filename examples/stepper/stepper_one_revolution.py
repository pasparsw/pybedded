from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    STEPS_PER_REVOLUTION: int = 200
    my_stepper: Stepper = Stepper(STEPS_PER_REVOLUTION, 8, 9, 10, 11)

    def setup() -> None:
        my_stepper.setSpeed(60)
        Serial.begin(9600)

    def loop() -> None:
        Serial.println("clockwise")
        my_stepper.step(STEPS_PER_REVOLUTION)
        delay(500)

        Serial.println("counterclockwise")
        my_stepper.step(-STEPS_PER_REVOLUTION)
        delay(500)
