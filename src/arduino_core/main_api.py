import logging

from typing import Any

from src.arduino_core.definitions import long

LOGGER = logging.getLogger("MainApi")

DEFAULT = 0
INTERNAL = 1
INTERNAL1V1 = 2
INTERNAL2V56 = 3
EXTERNAL = 4

AR_DEFAULT = 0
AR_INTERNAL = 1
AR_INTERNAL_1_5V = 2
AR_INTERNAL_2_0V = 3
AR_INTERNAL_2_5V = 4
AR_EXTERNAL = 5

VDD = 0
INTERNAL0V55 = 1
INTERNAL1V5 = 2
INTERNAL2V5 = 3
EXTERNAL4V3 = 4

AR_VDD = 0
AR_INTERNAL1V2 = 1
AR_INTERNAL2V4 = 2

def pinMode(pin: int, mode: int) -> None:
    LOGGER.info(f"Setting mode of pin {pin} to {mode}")

def digitalRead(pin: int) -> int:
    LOGGER.info(f"Reading state of pin {pin}")
    return 0

def digitalWrite(pin: int, state: int) -> None:
    LOGGER.info(f"Setting state of pin {pin} to {state}")

def analogRead(pin: int) -> int:
    LOGGER.info(f"Reading ADC value at pin {pin}")
    return 0

def analogReadResolution(bits: int) -> None:
    pass

def analogReference(mode: int) -> None:
    pass

def analogWrite(pin: int, value: int) -> None:
    LOGGER.info(f"Setting PWM at pin {pin} to {value}")

def analogWriteResolution(bits: int) -> None:
    pass

def delay(time_in_ms: int) -> None:
    LOGGER.info(f"Waiting {time_in_ms}ms")

def millis() -> long:
    LOGGER.info(f"Getting current timestamp")
    return 0

def micros() -> long:
    return 0

def map(value: int, from_low: int, from_high: int, to_low: int, to_high: int) -> int:
    LOGGER.info(f"Mapping value {value} from range {from_low}-{from_high} to range {to_low}-{to_high}")
    return 0

def constrain(value: int, range_low: int, range_high: int) -> int:
    LOGGER.info(f"Constraining value {value} to range {range_low}-{range_high}")
    return 0

def sizeof(obj: Any) -> int:
    LOGGER.info(f"Getting size of {obj}")
    return 0

def abs(value: int) -> int:
    return 0

def max(a: int, b: int) -> int:
    return 0

def min(a: int, b: int) -> int:
    return 0

def pow(base: int, exponent: int) -> int:
    return 0

def sq(value: int) -> int:
    return 0

def sqrt(value: int) -> int:
    return 0

def bit(position: int) -> int:
    return 0

def bitClear(value: int, position: int) -> int:
    return 0

def bitRead(value: int, position: int) -> int:
    return 0

def bitSet(value: int, position: int) -> int:
    return 0

def bitWrite(value: int, position: int, bit_value: int) -> int:
    return 0

def highByte(value: int) -> int:
    return 0

def lowByte(value: int) -> int:
    return 0

def cos(angle: int) -> float:
    return 0

def sin(angle: int) -> float:
    return 0

def tan(angle: int) -> float:
    return 0

def attachInterrupt(pin: int, function: Any, mode: int) -> None:
    pass

def detachInterrupt(pin: int) -> None:
    pass

def digitalPinToInterrupt(pin: int) -> int:
    return 0

def noTone(pin: int) -> None:
    pass

def pulseIn(pin: int, state: int, timeout: long = 1000000) -> long:
    return 0

def pulseInLong(pin: int, state: int, timeout: long = 1000000) -> long:
    return 0

def shiftIn(data_pin: int, clock_pin: int, bit_order: int) -> int:
    return 0

def shiftOut(data_pin: int, clock_pin: int, bit_order: int, value: int) -> None:
    pass

def tone(pin: int, frequency: int, duration: long = 0) -> None:
    pass

def isAlpha(c: str) -> bool:
    return False

def isAlphaNumeric(c: str) -> bool:
    return False

def isAscii(c: str) -> bool:
    return False

def isControl(c: str) -> bool:
    return False

def isDigit(c: str) -> bool:
    return False

def isGraph(c: str) -> bool:
    return False

def isHexadecimalDigit(c: str) -> bool:
    return False

def isLowerCase(c: str) -> bool:
    return False

def isPrintable(c: str) -> bool:
    return False

def isPunct(c: str) -> bool:
    return False

def isSpace(c: str) -> bool:
    return False

def isUpperCase(c: str) -> bool:
    return False

def isWhitespace(c: str) -> bool:
    return False

def interrupts() -> None:
    pass

def noInterrupts() -> None:
    pass

def delayMicroseconds(us: int) -> None:
    pass

def random(max: int, min: int = 0) -> int:
    return 0

def randomSeed(seed: int) -> None:
    pass


