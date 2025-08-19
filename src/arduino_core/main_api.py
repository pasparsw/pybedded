from src.arduino_core.definitions import long

def pinMode(pin: int, mode: int) -> None:
    pass

def digitalRead(pin: int) -> int:
    return 0

def digitalWrite(pin: int, state: int) -> None:
    pass

def analogRead(pin: int) -> int:
    return 0

def analogWrite(pin: int, value: int) -> None:
    pass

def delay(time_in_ms: int) -> None:
    pass

def millis() -> long:
    pass

def map(value: int, from_low: int, from_high: int, to_low: int, to_high: int) -> int:
    pass

def constrain(value: int, range_low: int, range_high: int) -> int:
    pass
