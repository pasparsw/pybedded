import os
import sys

PYTHON_2_ARDUINO_DIR: str = os.path.dirname(os.path.realpath(__file__))
sys.path.append(PYTHON_2_ARDUINO_DIR)

from .src.arduino_core.definitions import *
from .src.arduino_core.main_api import *
from .src.arduino_core.serial import *
from .src.arduino_board import *