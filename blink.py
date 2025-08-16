from arduino import *

with Arduino("some port", "uno"):
    def setup() -> None:
        pinMode(LED_BUILTIN, OUTPUT)

    def loop() -> None:
        digitalWrite(LED_BUILTIN, HIGH)
        delay(1000)
        digitalWrite(LED_BUILTIN, LOW)
        delay(1000)
