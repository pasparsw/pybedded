from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    RS: int = 12
    EN: int = 11
    D4: int = 5
    D5: int = 4
    D6: int = 3
    D7: int = 2

    lcd: LiquidCrystal = LiquidCrystal(RS, EN, D4, D5, D6, D7)

    def setup() -> None:
        lcd.begin(16, 2)
        Serial.begin(9600)

    def loop() -> None:
        if Serial.available():
            delay(100)
            lcd.clear()

            while Serial.available():
                lcd.write(Serial.read())
