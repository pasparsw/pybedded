from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.NANO_OLD_BOOTLOADER):
    def setup() -> None:
        Wire.begin()

        Serial.begin(9600)
        while not Serial:
            pass

        Serial.println("\nI2C Scanner")

    def loop() -> None:
        n_devices: int = 0

        Serial.println("Scanning...")

        for address in range(1, 127):
            Wire.beginTransmission(address)
            error: byte = Wire.endTransmission()

            if error == 0:
                Serial.print("I2C device found at address 0x")
                if address < 16:
                    Serial.print("0")
                Serial.print(address, HEX)
                Serial.println(" !")

                n_devices += 1
            elif error == 4:
                Serial.print("Unknown error at address 0x")
                if address < 16:
                    Serial.print("0")
                Serial.println(address, HEX)

        if n_devices == 0:
            Serial.println("No I2C devices found\n")
        else:
            Serial.println("Done\n")

        delay(5000)
