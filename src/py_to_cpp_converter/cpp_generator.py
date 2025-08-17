from src.py_to_cpp_converter.models.code_object import CodeObject
from src.py_to_cpp_converter.models.for_loop import ForLoop
from src.py_to_cpp_converter.models.function_call import FunctionCall
from src.py_to_cpp_converter.models.function_definition import FunctionDefinition
from src.py_to_cpp_converter.models.if_statement import IfStatement
from src.py_to_cpp_converter.models.variable_assignment import VariableAssignment
from src.py_to_cpp_converter.models.variable_definition import VariableDefinition


class CppGenerator:
    @staticmethod
    def generate(model: CodeObject, depth: int) -> str:
        cpp_code: str = ""
        indentation: str = " " * depth * 4

        for code_object in model.content:
            if isinstance(code_object, FunctionDefinition):
                args = ""

                for arg in code_object.arguments:
                    args += f"{arg.type} {arg.name}, "

                cpp_code += f"{indentation}{code_object.return_type} {code_object.name}({args.rstrip(", ")})\n{indentation}{{\n"
                cpp_code += CppGenerator.generate(code_object, depth + 1)
                cpp_code += f"{indentation}}}\n"
            elif isinstance(code_object, ForLoop):
                cpp_code += f"{indentation}for (int i={code_object.start_index}; i<{code_object.end_index}; i += {code_object.step})\n{indentation}{{\n"
                cpp_code += CppGenerator.generate(code_object, depth + 1)
                cpp_code += f"{indentation}}}\n"
            elif isinstance(code_object, IfStatement):
                cpp_code += f"{indentation}if ({code_object.condition.replace(" AND ", " && ").replace(" OR ", " || ")})\n{indentation}{{\n"
                cpp_code += CppGenerator.generate(code_object, depth + 1)
                cpp_code += f"{indentation}}}\n"
            elif isinstance(code_object, FunctionCall):
                cpp_code += f"{indentation}{code_object.call};\n"
            elif isinstance(code_object, VariableDefinition):
                if code_object.is_compile_time:
                    cpp_code += f"#define {code_object.name} {code_object.value}\n"
                else:
                    cpp_code += f"{indentation}{code_object.type} {code_object.name} = {code_object.value};\n"
            elif isinstance(code_object, VariableAssignment):
                cpp_code += f"{code_object.name} = {code_object.value};\n"

        return cpp_code
