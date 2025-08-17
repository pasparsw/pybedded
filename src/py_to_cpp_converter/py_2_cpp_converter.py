from typing import List

from src.py_to_cpp_converter.cpp_generator import CppGenerator
from src.py_to_cpp_converter.models.code_object import CodeObject
from src.py_to_cpp_converter.python_parser import PythonParser


class Py2CppConverter:
    @staticmethod
    def convert(python_code: List[str]) -> str:
        model: CodeObject = CodeObject(content=[])
        model = PythonParser.build_model(model, python_code)
        cpp_code: str = CppGenerator.generate(model, depth=0)

        print(cpp_code)

        return cpp_code
