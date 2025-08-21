import logging

from typing import List

from src.py_to_cpp_converter.models.code_object import CodeObject
from src.py_to_cpp_converter.models.else_block import ElseBlock
from src.py_to_cpp_converter.models.for_loop import ForLoop
from src.py_to_cpp_converter.models.function_call import FunctionCall
from src.py_to_cpp_converter.models.function_definition import FunctionArgument, FunctionDefinition
from src.py_to_cpp_converter.models.if_statement import IfStatement
from src.py_to_cpp_converter.models.return_statement import ReturnStatement
from src.py_to_cpp_converter.models.variable_modification import VariableModification
from src.py_to_cpp_converter.models.variable_definition import VariableDefinition
from src.py_to_cpp_converter.models.while_loop import WhileLoop

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


def is_variable_modification(python_line: str) -> bool:
    return " = " in python_line or " += " in python_line or " -= " in python_line or " *= " in python_line \
        or " /= " in python_line

def is_else_block(python_line: str) -> bool:
    return "else" in python_line

def is_comment(python_line: str) -> bool:
    return python_line.lstrip().startswith("#")

def is_while_loop(python_line: str) -> bool:
    return "while " in python_line

def is_return_statement(python_line: str) -> bool:
    return "return " in python_line

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

            if is_comment(python_line):
                line_number += 1
                continue
            elif is_function_definition(python_line):
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
            elif is_while_loop(python_line):
                LOGGER.debug(f"Found while loop at line {line_number}")
                line_number = PythonParser.__parse_while_loop(root_object, python_line, python_code, line_number)
                continue
            elif is_variable_definition(python_line):
                LOGGER.debug(f"Found variable definition at line {line_number}")
                PythonParser.__parse_variable_definition(root_object, python_line)
            elif is_function_call(python_line):
                LOGGER.debug(f"Found function call at line {line_number}")
                root_object.content.append(FunctionCall(content=[], call=python_line.lstrip()))
            elif is_variable_modification(python_line):
                LOGGER.debug(f"Found variable modification at line {line_number}")
                PythonParser.__parse_variable_modification(root_object, python_line)
            elif is_else_block(python_line):
                LOGGER.debug(f"Found else block at line {line_number}")
                line_number = PythonParser.__parse_else_block(root_object, python_code, line_number)
                continue
            elif is_return_statement(python_line):
                LOGGER.debug(f"Found return statement at line {line_number}")
                PythonParser.__parse_return_statement(root_object, python_line)

            line_number += 1

        LOGGER.debug("Parsing done")

        return root_object

    @staticmethod
    def get_dependencies(python_code: List[str]) -> List[str]:
        dependencies: List[str] = []

        for line in python_code:
            if "EEPROM" in line and "EEPROM" not in dependencies:
                dependencies.append("EEPROM")
            if ": Servo" in line and "Servo" not in dependencies:
                dependencies.append("Servo")
            if ": SoftwareSerial" in line and "SoftwareSerial" not in dependencies:
                dependencies.append("SoftwareSerial")

        return dependencies

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
        variable_name: str = python_line.lstrip().split("for ")[1].split(" in")[0]
        start: str = ""
        end: str = ""
        step: str = ""

        range_content: str = python_line.split("in range(")[1].split("):")[0]
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

        for_loop = ForLoop(content=[], iter_var_name=variable_name, start_index=start, end_index=end, step=step)
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
        is_array: bool = "List[" in python_line
        array_size: str = ""
        array_content: str = ""

        variable_name: str = python_line.split(":")[0]
        variable_value: str = python_line.split("= ")[1]
        variable_type: str = python_line.split(": ")[1].split(" =")[0]

        if is_array:
            variable_type = variable_type.split("[")[1].split("]")[0]
            variable_value = variable_value.split(" #")[0]
            if "# max=" in python_line:
                array_size = python_line.split("# max=")[1]
            else:
                array_content = python_line.split("] = [")[1].split("]")[0]

        variable_definition = VariableDefinition(content=[], name=variable_name.lstrip(), type=variable_type,
                                                 value=variable_value, is_compile_time=variable_name.isupper(),
                                                 is_array=is_array, array_size=array_size, array_content=array_content)
        LOGGER.debug(f"Parsed variable definition model: {variable_definition}")

        root_object.content.append(variable_definition)

    @staticmethod
    def __parse_variable_modification(root_object: CodeObject, python_line: str) -> None:
        variable_name: str = python_line.lstrip().split(" ")[0]
        operator: str = python_line.lstrip().split(" ")[1].split(" ")[0]
        variable_value: str = python_line.lstrip().split(" ")[2]

        variable_modification = VariableModification(content=[], name=variable_name.lstrip(), operator=operator,
                                                     value=variable_value)
        LOGGER.debug(f"Parsed variable modification model: {variable_modification}")

        root_object.content.append(variable_modification)

    @staticmethod
    def __parse_else_block(root_object: CodeObject, python_code: List[str], line_number: int) -> int:
        else_block = ElseBlock(content=[])
        LOGGER.debug(f"Parsed else block model: {else_block}")

        else_block_end_line: int = get_block_end_line(line_number, python_code)
        LOGGER.debug(f"Else block body ends at line {else_block_end_line}")

        root_object.content.append(PythonParser.build_model(else_block,
                                                            python_code[line_number + 1:else_block_end_line]))
        return else_block_end_line

    @staticmethod
    def __parse_while_loop(root_object: CodeObject, python_line: str, python_code: List[str], line_number: int) -> int:
        condition: str = python_line.split("while ")[1].split(":")[0].replace(" and ", " AND ").replace(" or ", " OR ")

        while_loop = WhileLoop(content=[], condition=condition)
        LOGGER.debug(f"Parsed while loop model: {while_loop}")

        while_loop_end_line: int = get_block_end_line(line_number, python_code)
        LOGGER.debug(f"While loop body ends at line {while_loop_end_line}")

        root_object.content.append(PythonParser.build_model(while_loop,
                                                            python_code[line_number + 1:while_loop_end_line]))
        return while_loop_end_line

    @staticmethod
    def __parse_return_statement(root_object: CodeObject, python_line: str) -> None:
        expression: str = python_line.split("return ")[1]

        return_statement = ReturnStatement(content=[], return_expression=expression)
        LOGGER.debug(f"Parsed return statement model: {return_statement}")

        root_object.content.append(return_statement)
