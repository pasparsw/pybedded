# pin modes
from enum import Enum

OUTPUT: int = 0
INPUT: int = 1
INPUT_PULLUP: int = 2

# pin states
LOW: int = 0
HIGH: int = 1

# analog pins IDs
A0 = 0
A1 = 1
A2 = 2
A3 = 3
A4 = 4
A5 = 5

# boards
class Boards(Enum):
    UNO = "arduino:avr:uno"
    NANO = "arduino:avr:nano"
    MEGA = "arduino:avr:mega"

# other
LED_BUILTIN: int = 0
