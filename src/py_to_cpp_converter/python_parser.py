import logging

from typing import List

from src.py_to_cpp_converter.models.code_object import CodeObject
from src.py_to_cpp_converter.models.for_loop import ForLoop
from src.py_to_cpp_converter.models.function_call import FunctionCall
from src.py_to_cpp_converter.models.function_definition import FunctionArgument, FunctionDefinition
from src.py_to_cpp_converter.models.if_statement import IfStatement
from src.py_to_cpp_converter.models.variable_assignment import VariableAssignment
from src.py_to_cpp_converter.models.variable_definition import VariableDefinition

LOGGER = logging.getLogger("PythonParser")


def is_function_definition(python_line: str) -> bool:
    return "def " in python_line and "(" in python_line and ")" in python_line


def is_for_loop(python_line: str) -> bool:
    return "for " in python_line and " in range(" in python_line


def is_if_statement(python_line: str) -> bool:
    return "if " in python_line


def is_function_call(python_line: str) -> bool:
    return "(" in python_line and ")" in python_line


def is_variable_definition(python_line: str) -> bool:
    return ": " in python_line and " = " in python_line


def is_variable_assignment(python_line: str) -> bool:
    return " = " in python_line


def get_block_end_line(line_number: int, python_code: List[str]) -> int:
    block_end_line = len(python_code)
    num_of_tabs: int = int((len(python_code[line_number]) - len(python_code[line_number].lstrip(" "))) / 4) + 1

    for i in range(line_number + 1, len(python_code)):
        current_num_of_tabs: int = int((len(python_code[i]) - len(python_code[i].lstrip(" "))) / 4)

        if current_num_of_tabs < num_of_tabs and i != len(python_code):
            if python_code[i] == "\n":
                next_num_of_tabs: int = int(
                    (len(python_code[i + 1]) - len(python_code[i + 1].lstrip(" "))) / 4)

                if next_num_of_tabs >= num_of_tabs:
                    continue

            block_end_line = i
            break

    return block_end_line


class PythonParser:
    @staticmethod
    def build_model(root_object: CodeObject, python_code: List[str]) -> CodeObject:
        LOGGER.info(f"Parsing Python code to build an intermediate model (root: {root_object})")

        line_number: int = 0

        while line_number < len(python_code):
            python_line: str = python_code[line_number].rstrip()

            if is_function_definition(python_line):
                LOGGER.debug(f"Found function definition at line {line_number}")
                line_number = PythonParser.__parse_function_definition(root_object, python_line, python_code, line_number)
                continue
            elif is_for_loop(python_line):
                LOGGER.debug(f"Found for loop at line {line_number}")
                line_number = PythonParser.__parse_for_loop(root_object, python_line, python_code, line_number)
                continue
            elif is_if_statement(python_line):
                LOGGER.debug(f"Found if statement at line {line_number}")
                line_number = PythonParser.__parse_if_statement(root_object, python_line, python_code, line_number)
                continue
            elif is_variable_definition(python_line):
                LOGGER.debug(f"Found variable definition at line {line_number}")
                PythonParser.__parse_variable_definition(root_object, python_line)
            elif is_function_call(python_line):
                LOGGER.debug(f"Found function call at line {line_number}")
                root_object.content.append(FunctionCall(content=[], call=python_line.lstrip()))
            elif is_variable_assignment(python_line):
                LOGGER.debug(f"Found variable assignment at line {line_number}")
                PythonParser.__parse_variable_assignment(root_object, python_line)

            line_number += 1

        LOGGER.debug("Parsing done")

        return root_object

    @staticmethod
    def __parse_function_definition(root_object: CodeObject, python_line: str, python_code: List[str],
                                    line_number: int) -> int:
        function_name: str = python_line.split("def ")[1].split("(")[0]
        function_return_type: str = python_line.split("-> ")[1].split(":")[0]
        function_return_type = "void" if function_return_type == "None" else function_return_type
        function_arguments: str = python_line.split("(")[1].split(")")[0]
        arg_name_type_pairs: List[str] = function_arguments.split(", ")
        arg_name_type_pairs = [] if arg_name_type_pairs == [''] else arg_name_type_pairs
        args: List[FunctionArgument] = []

        for element in arg_name_type_pairs:
            args.append(FunctionArgument(name=element.split(": ")[0], type=element.split(": ")[1]))

        function_definition = FunctionDefinition(content=[], name=function_name, arguments=args,
                                                 return_type=function_return_type)
        LOGGER.debug(f"Parsed function definition mode: {function_definition}")

        function_def_end_line: int = get_block_end_line(line_number, python_code)
        LOGGER.debug(f"Function body ends at line {function_def_end_line}")

        root_object.content.append(PythonParser.build_model(function_definition,
                                                         python_code[line_number + 1:function_def_end_line]))
        return function_def_end_line

    @staticmethod
    def __parse_for_loop(root_object: CodeObject, python_line: str, python_code: List[str],
                         line_number: int) -> int:
        start: str = ""
        end: str = ""
        step: str = ""

        range_content: str = python_line.split("in range(")[1].split(")")[0]
        range_content = [] if range_content == [''] else range_content
        range_params: List[str] = range_content.split(", ")

        if len(range_params) == 1:
            start = "0"
            end = range_params[0]
            step = "1"
        elif len(range_params) == 2:
            start = range_params[0]
            end = range_params[1]
            step = "1"
        elif len(range_params) == 3:
            start = range_params[0]
            end = range_params[1]
            step = range_params[2]

        for_loop = ForLoop(content=[], start_index=start, end_index=end, step=step)
        LOGGER.debug(f"Parsed for loop model: {for_loop}")

        for_loop_end_line: int = get_block_end_line(line_number, python_code)
        LOGGER.debug(f"For loop body ends at line {for_loop_end_line}")

        root_object.content.append(PythonParser.build_model(for_loop,
                                                         python_code[line_number + 1:for_loop_end_line]))
        return for_loop_end_line

    @staticmethod
    def __parse_if_statement(root_object: CodeObject, python_line: str, python_code: List[str],
                             line_number: int) -> int:
        condition: str = python_line.split("if ")[1].split(":")[0].replace(" and ", " AND ").replace(" or ", " OR ")

        if_statement = IfStatement(content=[], condition=condition)
        LOGGER.debug(f"Parsed if statement model: {if_statement}")

        if_statement_end_line: int = get_block_end_line(line_number, python_code)
        LOGGER.debug(f"If statement body ends at line {if_statement_end_line}")

        root_object.content.append(PythonParser.build_model(if_statement,
                                                         python_code[line_number + 1:if_statement_end_line]))
        return if_statement_end_line

    @staticmethod
    def __parse_variable_definition(root_object: CodeObject, python_line: str) -> None:
        variable_name: str = python_line.split(":")[0]
        variable_value: str = python_line.split("= ")[1]
        variable_type: str = python_line.split(": ")[1].split(" =")[0]

        variable_definition = VariableDefinition(content=[], name=variable_name.lstrip(), type=variable_type,
                                                 value=variable_value, is_compile_time=variable_name.isupper())
        LOGGER.debug(f"Parsed variable definition mode: {variable_definition}")

        root_object.content.append(variable_definition)

    @staticmethod
    def __parse_variable_assignment(root_object: CodeObject, python_line: str) -> None:
        variable_name: str = python_line.split(" =")[0]
        variable_value: str = python_line.split("= ")[1]

        variable_assignment = VariableAssignment(content=[], name=variable_name, value=variable_value)
        LOGGER.debug(f"Parsed variable assignment model: {variable_assignment}")

        root_object.content.append(variable_assignment)
