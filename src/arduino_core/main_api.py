import logging

from typing import Any

from src.arduino_core.definitions import long

LOGGER = logging.getLogger("MainApi")

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

def analogWrite(pin: int, value: int) -> None:
    LOGGER.info(f"Setting PWM at pin {pin} to {value}")

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
