#include <Keyboard.h>
void setup() {
    Serial.begin(9600);
    Keyboard.begin();
}
void loop() {
    if (Serial.available()) {
        char in_char = Serial.read();
        Keyboard.write(in_char + 1);
    }
}
