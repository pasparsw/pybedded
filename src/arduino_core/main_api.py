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
