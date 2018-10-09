#   Primary Author: Aadesh M Bagmar <aadeshbagmar@gmail.com>
#
#   Purpose: File to analyze a given file using Abstract Syntax Tree

import ast

from pathlib import Path
from typing import Union, List, Dict
from QuickUI.function_support import check_function

class IncorrectArgument(Exception):
    pass

class IncorrectFileType(Exception):
    pass


class ExtractArgs:
    def __init__(self, file_path: Union[str, Path])->None:
        """
        Init function for the extractor

        Args:
            file_path Union[str, Path]: Full path to the script from which we wish to create a UI.

        Returns:
            None
        """
        if isinstance(file_path, str):
            file_path = Path(file_path)

        if not isinstance(file_path, Path):
            raise IncorrectArgument

        if not file_path.exists():
            raise FileNotFoundError

        if ".py" not in file_path.suffix:
            raise IncorrectFileType

        self.file_path = file_path

    def _create_ast_node(self)->ast:
        """
        Function to create an ast node object from the given file poth

        Returns:
            An ast CodeType object
        """
        ast_head = compile(open(str(self.file_path), 'rb').read(), file_path, 'exec', ast.PyCF_ONLY_AST)
        return ast_head

    @staticmethod
    def _filter(element)->bool:
        """
        Applies checks to see if the element value / class matches the criteria for finding the add_argument attribute

        Args:
            element: ast node

        Returns:
            True or False indicating whether this element is our add_argument element.
        """
        # 1. Check if it has the value attribute that we can extract
        if "value" not in element._fields:
            return False

        # 2. Check if the element contains a function field
        if "func" not in element.value._fields:
            return False

        # 3. Check if the element type is callable
        if not isinstance(element.value, ast.Call):
            return False

        # 4. Check if "attr" field exists in this
        if "attr" not in element.value.func._fields:
            return False

        # 5. Check if "add_argument" exists
        if element.value.func.attr != "add_argument":
            return False

        # 6. Find the parameter name
        if 0 < len(element.value.args) > 1:
            return False

        return True

    @staticmethod
    def _extractor(parser_value_arg)->Dict:
        """
        Function to extract the value depending on the data type. In some cases, the function
        might be called recursively as well.

        Args:
            parser_value_arg: Element node to be extracted

        Returns:
            Extracted value
        """

        if isinstance(parser_value_arg, ast.Str):
            parsed_value = parser_value_arg.s

        elif isinstance(parser_value_arg, ast.Name):
            parsed_value = parser_value_arg.id

        elif isinstance(parser_value_arg, ast.NameConstant):
            parsed_value = parser_value_arg.value

        elif isinstance(parser_value_arg, ast.List):
            parsed_value = [ExtractArgs._extractor(x) for x in parser_value_arg.elts]

        elif isinstance(parser_value_arg, ast.Call):
            parsed_value = check_function(parser_value_arg)

        else:
            parsed_value = "Unknown Type"

        return parsed_value

    @staticmethod
    def _extract_params(element)->Dict:
        """
        Function to extract the add_argument parameters once they pass the filter.

        Args:
            element: AST node

        Returns:
            Dictionary containing the extracted values.
        """
        argument = element.value.args
        keywords = element.value.keywords
        parser_details = {"parameter": argument[0].s}

        for keyword in keywords:
            parser_key = keyword.arg
            parser_value_arg = keyword.value
            parsed_value = ExtractArgs._extractor(parser_value_arg)

            parser_details[parser_key] = parsed_value
        return parser_details

    @staticmethod
    def _bfs(bfs_list: List)->List:
        """
        Runs a BFS on the code to extract all the argparse variables

        Args:
            bfs_list: Needs the body of the AST tree as a list.

        Returns:
            List of parsed arguments
        """
        parser_argument_list = []

        i = 0
        while True:
            if i >= len(bfs_list):
                break

            element = bfs_list[i]
            i += 1

            # 1. Skip if there are any imports
            if element.__class__ == ast.Import or element.__class__ == ast.ImportFrom:
                continue

            # 2. Check for "if" class
            if element.__class__ == ast.If:
                bfs_list.extend(element.body)

            # 3. Check for "functionDef" class
            if isinstance(element, ast.FunctionDef):
                bfs_list.extend(element.body)

            # 4. Apply a filter to extract relevant elements.
            if not ExtractArgs._filter(element):
                continue

            # 5. Extract the parameters from the given argument.
            parser_argument_list.append(ExtractArgs._extract_params(element))

        return parser_argument_list


    def find_args(self)->List:
        """
        Run a breadth first search to extract all the args and their parameters.

        Returns:
            List of Dictionaries. Each dictionary has the keys - parameter, help, type, required.
        """
        # 1. Create the AST Node
        ast_head = self._create_ast_node()

        # 2. Create a list of "body" elements
        bfs_list = ast_head.body.copy()

        # 3. Apply BFS and extract parameters.
        parser_argument_list = self._bfs(bfs_list)

        return parser_argument_list

if __name__ == '__main__':
    file_path = "../examples/choices_test.py"
    ea = ExtractArgs(file_path)
    print(ea.find_args())

