import inspect

from inspect import FrameInfo
from typing import Tuple, List

FilePath = str
LineNumber = int

HIGH: int = 1
LOW: int = 0
OUTPUT: int = 0
INPUT: int = 1
INPUT_PULLUP: int = 2
LED_BUILTIN: int = 0

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

class Serial:
    @staticmethod
    def begin(baudrate: int) -> int:
        pass

    @staticmethod
    def available() -> bool:
        pass

    @staticmethod
    def print(message: str) -> None:
        pass

    @staticmethod
    def println(message: str) -> None:
        pass

    @staticmethod
    def read() -> str:
        pass

    @staticmethod
    def write(self) -> str:
        pass

class Arduino:
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
        ino_file_path: str = self.__create_ino_file(cpp_code)

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

        cpp_code = self.__parse_block(python_code, indentation="")

        print(cpp_code)

        return cpp_code

    def __create_ino_file(self, cpp_code) -> str:
        print(f"Creating .ino file")
        return ""

    def __compile_ino_file(self, ino_file_path: str) -> None:
        print(f"Compiling...")
        pass

    def __flash_arduino(self) -> None:
        print(f"Flashing...")
        pass

    def __parse_block(self, python_code: List[str], indentation: str) -> str:
        cpp_code: str = ""
        line_number: int = 0

        while line_number < len(python_code):
            python_line: str = python_code[line_number].rstrip()
            # function definition
            if "def " in python_line and "(" in python_line and ")" in python_line:
                function_name: str = python_line.split("def ")[1].split("(")[0]
                function_arguments: str = python_line.split("(")[1].split(")")[0]
                function_return_type: str = python_line.split("-> ")[1].split(":")[0]
                function_return_type = "void" if function_return_type == "None" else function_return_type
                num_of_tabs: int = int((len(python_line) - len(python_line.lstrip(" ")))/4) + 1
                function_body_end_line = len(python_code)

                for i in range(line_number + 1, len(python_code)):
                    current_num_of_tabs: int = int((len(python_code[i]) - len(python_code[i].lstrip(" ")))/4)

                    if current_num_of_tabs < num_of_tabs and i != len(python_code):
                        next_num_of_tabs: int = int((len(python_code[i + 1]) - len(python_code[i + 1].lstrip(" ")))/4)

                        if next_num_of_tabs < num_of_tabs:
                            function_body_end_line = i
                            break

                current_indentation: str = indentation + "    "
                cpp_code += f"{function_return_type} {function_name}({function_arguments})\n{{\n"
                cpp_code += self.__parse_block(python_code[line_number + 1:function_body_end_line], current_indentation)
                cpp_code += "}\n"
                line_number = function_body_end_line
                continue
            # function call
            elif "(" in python_line and ")" in python_line:
                cpp_code += f"{indentation}{python_line.lstrip()};\n"
            # variable definition
            elif ": " in python_line and " = " in python_line:
                variable_name: str = python_line.split(":")[0]
                variable_type: str = python_line.split(": ")[1].split(" =")[0]
                variable_value: str = python_line.split("= ")[1]

                cpp_code += f"{indentation}{variable_type} {variable_name.lstrip()} = {variable_value};\n"
            # variable assignment
            elif " = " in python_line:
                variable_name: str = python_line.split(" =")[0]
                variable_value: str = python_line.split("= ")[1]

                cpp_code += f"{indentation}{variable_name.lstrip()} = {variable_value};\n"
            # python global variable
            elif "global " in python_line:
                line_number += 1
                continue
            # incrementation
            elif " += " in python_line:
                cpp_code += f"{indentation}{python_line.lstrip()};\n"
            # if statement
            elif "if " in python_line:
                condition: str = python_line.split("if ")[1].split(":")[0]
                cpp_code += f"{indentation}if ({condition})\n{indentation}{{\n"
                num_of_tabs: int = int((len(python_line) - len(python_line.lstrip(" "))) / 4) + 1
                if_statement_body_end_line = len(python_code)

                for i in range(line_number + 1, len(python_code)):
                    current_num_of_tabs: int = int((len(python_code[i]) - len(python_code[i].lstrip(" "))) / 4)

                    if current_num_of_tabs < num_of_tabs and i != len(python_code):
                        if python_code[i] == "\n":
                            next_num_of_tabs: int = int((len(python_code[i + 1]) - len(python_code[i + 1].lstrip(" "))) / 4)

                            if next_num_of_tabs > num_of_tabs:
                                continue

                        if_statement_body_end_line = i
                        break

                current_indentation: str = indentation + "    "
                cpp_code += self.__parse_block(python_code[line_number + 1:if_statement_body_end_line], current_indentation)
                cpp_code += f"{indentation}}}\n"
                line_number = if_statement_body_end_line
                continue

            line_number += 1

        return cpp_code
