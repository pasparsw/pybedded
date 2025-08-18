import os
import sys

PYBEDDED_DIR: str = os.path.dirname(os.path.realpath(__file__))
sys.path.append(PYBEDDED_DIR)

from .src.arduino_board import ArduinoBoard
from .src.arduino_core.definitions import *
from .src.arduino_core.main_api import *
from .src.arduino_core.serial import *
