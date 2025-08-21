from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    myservo: Servo = Servo()
    pos: int = 0

    def setup() -> None:
        myservo.attach(9)

    def loop() -> None:
        for pos in range(180):
            myservo.write(pos)
            delay(15)
        for pos in range(180, 0, -1):
            myservo.write(pos)
            delay(15)
