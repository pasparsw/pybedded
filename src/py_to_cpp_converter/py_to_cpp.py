from typing import List


class PyToCpp:
    @staticmethod
    def convert(python_code: List[str], indentation: str) -> str:
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
                    current_num_of_tabs: int = int((len(python_code[i]) - len(python_code[i].lstrip(" "))) / 4)

                    if current_num_of_tabs < num_of_tabs and i != len(python_code):
                        if python_code[i] == "\n":
                            next_num_of_tabs: int = int((len(python_code[i + 1]) - len(python_code[i + 1].lstrip(" "))) / 4)

                            if next_num_of_tabs >= num_of_tabs:
                                continue

                        function_body_end_line = i
                        break

                current_indentation: str = indentation + "    "
                cpp_code += f"{function_return_type} {function_name}({function_arguments})\n{{\n"
                cpp_code += PyToCpp.convert(python_code[line_number + 1:function_body_end_line], current_indentation)
                cpp_code += "}\n"
                line_number = function_body_end_line
                continue
            # for loop
            elif "for " in python_line and " in range(" in python_line:
                loop_range: str = python_line.split(" in range(")[1].split(")")[0]
                cpp_code += f"{indentation}for (i=0; i<{loop_range}; i++)\n{indentation}{{\n"
                num_of_tabs: int = int((len(python_line) - len(python_line.lstrip(" "))) / 4) + 1
                for_loop_body_end_line = len(python_code)

                for i in range(line_number + 1, len(python_code)):
                    current_num_of_tabs: int = int((len(python_code[i]) - len(python_code[i].lstrip(" "))) / 4)

                    if current_num_of_tabs < num_of_tabs and i != len(python_code):
                        if python_code[i] == "\n":
                            next_num_of_tabs: int = int(
                                (len(python_code[i + 1]) - len(python_code[i + 1].lstrip(" "))) / 4)

                            if next_num_of_tabs >= num_of_tabs:
                                continue

                        for_loop_body_end_line = i
                        break

                current_indentation: str = indentation + "    "
                cpp_code += PyToCpp.convert(python_code[line_number + 1:for_loop_body_end_line], current_indentation)
                cpp_code += f"{indentation}}}\n"
                line_number = for_loop_body_end_line
                continue
            # function call
            elif "(" in python_line and ")" in python_line:
                cpp_code += f"{indentation}{python_line.lstrip()};\n"
            # variable definition
            elif ": " in python_line and " = " in python_line:
                variable_name: str = python_line.split(":")[0]
                variable_value: str = python_line.split("= ")[1]
                variable_type: str = python_line.split(": ")[1].split(" =")[0]

                if variable_name.isupper():
                    cpp_code += f"#define {variable_name.lstrip()} {variable_value}\n"
                else:
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

                            if next_num_of_tabs >= num_of_tabs:
                                continue

                        if_statement_body_end_line = i
                        break

                current_indentation: str = indentation + "    "
                cpp_code += PyToCpp.convert(python_code[line_number + 1:if_statement_body_end_line], current_indentation)
                cpp_code += f"{indentation}}}\n"
                line_number = if_statement_body_end_line
                continue

            line_number += 1

        return cpp_code