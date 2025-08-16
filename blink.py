from arduino import *

with Arduino("some port", "uno"):
    counter: int = 0

    def setup() -> None:
        global counter

        Serial.begin(9600)
        pinMode(LED_BUILTIN, OUTPUT)
        counter = 12

    def loop() -> None:
        global counter

        digitalWrite(LED_BUILTIN, HIGH)
        delay(1000)
        digitalWrite(LED_BUILTIN, LOW)
        delay(1000)

        counter += 1

        if counter < 15:
            Serial.println("Counter lower than 15")
        if counter == 15:
            Serial.println("Counter equal to 15")
        if counter > 15:
            Serial.println("Counter greater than 15")
