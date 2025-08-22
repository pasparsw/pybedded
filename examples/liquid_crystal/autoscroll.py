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

    def loop() -> None:
        lcd.setCursor(0, 0)

        for this_char in range(10):
            lcd.print(this_char)
            delay(500)

        lcd.setCursor(16, 1)
        lcd.autoscroll()

        for this_char in range(10):
            lcd.print(this_char)
            delay(500)

        lcd.noAutoscroll()
        lcd.clear()
