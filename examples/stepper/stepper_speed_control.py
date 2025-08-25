from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    STEPS_PER_REVOLUTION: int = 200
    my_stepper: Stepper = Stepper(STEPS_PER_REVOLUTION, 8, 9, 10, 11)

    def setup() -> None:
        pass

    def loop() -> None:
        sensor_reading: int = analogRead(A0)
        motor_speed: int = map(sensor_reading, 0, 1023, 0, 100)

        if motor_speed > 0:
            my_stepper.setSpeed(motor_speed)
            my_stepper.step(STEPS_PER_REVOLUTION / 100)
