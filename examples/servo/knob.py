# prerequisite: arduino-cli lib install Servo

from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    myservo: Servo = Servo()

    potpin: int = A0
    val: int = 0

    def setup() -> None:
        myservo.attach(9)

    def loop() -> None:
        global val

        val = analogRead(potpin)
        val = map(val, 0, 1023, 0, 180)
        myservo.write(val)
        delay(15)
