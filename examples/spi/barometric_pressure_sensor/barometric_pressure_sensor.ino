#include <SPI.h>
#define PRESSURE 0x1F
#define PRESSURE_LSB 0x20
#define TEMPERATURE 0x21
#define READ 0b11111100
#define WRITE 0b00000010
#define DATA_READY_PIN 6
#define CHIP_SELECT_PIN 7
void write_register(byte this_register, byte value) {
    this_register = this_register << 2;
    byte data_to_send = this_register | WRITE;
    digitalWrite(CHIP_SELECT_PIN, LOW);
    SPI.transfer(data_to_send);
    SPI.transfer(value);
    digitalWrite(CHIP_SELECT_PIN, HIGH);
}
unsigned int read_register(byte this_register, int bytes_to_read) {
    Serial.print(this_register, BIN);
    Serial.print("\t");
    this_register = this_register << 2;
    byte data_to_send = this_register & READ;
    Serial.println(this_register, BIN);
    digitalWrite(CHIP_SELECT_PIN, LOW);
    SPI.transfer(data_to_send);
    unsigned int result = SPI.transfer(0x00);
    bytes_to_read -= 1;
    if (bytes_to_read > 0) {
        result = result << 8;
        byte in_byte = SPI.transfer(0x00);
        result = result | in_byte;
        bytes_to_read -= 1;
    }
    digitalWrite(CHIP_SELECT_PIN, HIGH);
    return result;
}
void setup() {
    Serial.begin(9600);
    SPI.begin();
    pinMode(DATA_READY_PIN, INPUT);
    pinMode(CHIP_SELECT_PIN, OUTPUT);
    write_register(0x02, 0x2D);
    write_register(0x01, 0x03);
    write_register(0x03, 0x02);
    delay(100);
}
void loop() {
    write_register(0x03, 0x0A);
    if (digitalRead(DATA_READY_PIN) == HIGH) {
        int temp_data = read_register(0x21, 2);
        float real_temp = temp_data/20.0;
        Serial.print("Temp[C]=");
        Serial.print(real_temp);
        byte pressure_data_high = read_register(0x1F, 1);
        unsigned int pressure_data_low = read_register(0x20, 2);
        long pressure = ((pressure_data_high << 16) | pressure_data_low) / 4;
        Serial.println("\tPressure [Pa]=" + String(pressure));
    }
}
