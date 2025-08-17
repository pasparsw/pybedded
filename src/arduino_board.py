import inspect
import os.path

from inspect import FrameInfo
from typing import Tuple, List

from src.py_to_cpp_converter.py_2_cpp_converter import Py2CppConverter
from src.arduino_core.definitions import *
from src.arduino_core.main_api import *
from src.arduino_core.serial import *

FilePath = str
LineNumber = int

class ArduinoBoard:
    def __init__(self, port: str, board_name: str):
        self.__port: str = port
        self.__board_name: str = board_name

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Starting Python-to-Arduino conversion")

        file_path, start_line = self.__get_callers_properties()
        python_code: List[str] = self.__load_arduino_python_code(file_path, start_line)
        cpp_code: str = self.__convert_python_to_cpp(python_code)
        ino_file_path: str = self.__create_ino_file(file_path, cpp_code)

        self.__compile_ino_file(ino_file_path)
        self.__flash_arduino()

        print("Done")

    def __get_callers_properties(self) -> Tuple[FilePath, LineNumber]:
        print("Getting properties of the Python script with Arduino code")
        frame: FrameInfo = inspect.stack()[2]

        return frame.filename, frame.lineno

    def __load_arduino_python_code(self, script_path: FilePath, python_code_start_line: LineNumber) -> List[str]:
        print(f"Loading Python Arduino code from {script_path} starting at {python_code_start_line}")

        with open(script_path) as file:
            return file.readlines()[python_code_start_line:]

    def __convert_python_to_cpp(self, python_code: List[str]) -> str:
        print(f"Converting Python code to C++")

        return Py2CppConverter.convert(python_code)

    def __create_ino_file(self, script_path: str, cpp_code: str) -> str:
        print(f"Creating .ino file")

        file_name: str = f"{os.path.basename(script_path).rstrip(".py")}.ino"
        dir_path: str = os.path.dirname(script_path)

        with open(os.path.join(dir_path, file_name), 'w') as file:
            file.write(cpp_code)

        return ""

    def __compile_ino_file(self, ino_file_path: str) -> None:
        print(f"Compiling...")
        pass

    def __flash_arduino(self) -> None:
        print(f"Flashing...")
        pass


