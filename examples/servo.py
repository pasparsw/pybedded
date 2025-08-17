with Arduino("some port", "uno"):
    ADC_PIN: int = A1
    LED_PIN: int = 8
    WARNING_LED_PIN: int = 9

    adc_value: int = 0

    def setup() -> None:
        Serial.begin(9600)
        pinMode(WARNING_LED_PIN, OUTPUT)
        digitalWrite(WARNING_LED_PIN, LOW)

    def loop() -> None:
        global adc_value

        adc_value = analogRead(ADC_PIN)
        analogWrite(LED_PIN, adc_value)

        if adc_value > 900:
            Serial.println("ADC value higher than 900! Pausing for 3 seconds...")

            for i in range(3):
                digitalWrite(WARNING_LED_PIN, HIGH)
                delay(500)
                digitalWrite(WARNING_LED_PIN, LOW)
                delay(500)
