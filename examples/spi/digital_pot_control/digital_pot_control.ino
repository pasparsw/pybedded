#include <SPI.h>
#define SLAVE_SELECT_PIN 10
void digital_pot_write(int address, int value) {
    digitalWrite(SLAVE_SELECT_PIN, LOW);
    delay(100);
    SPI.transfer(address);
    SPI.transfer(value);
    delay(100);
    digitalWrite(SLAVE_SELECT_PIN, HIGH);
}
void setup() {
    pinMode(SLAVE_SELECT_PIN, OUTPUT);
    SPI.begin();
}
void loop() {
    for (int channel=0; channel<6; channel += 1) {
        for (int level=0; level<255; level += 1) {
            digital_pot_write(channel, level);
            delay(10);
        }
        delay(100);
        for (int level=0; level<255; level += 1) {
            digital_pot_write(channel, 255 - level);
            delay(10);
        }
    }
}
