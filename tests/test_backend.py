#   Primary Author: Aadesh M Bagmar <aadeshbagmar@gmail.com>
#
#   Purpose: A short description of the purpose of this source file ...

from QuickUI.analyzer import ExtractArgs

def test_basics():
    """
    Test the basic functionality when the argparse is present inside the main function
    """
    file_path = "tests/files/basic_test.py"
    e = ExtractArgs(file_path)

    assert(e.find_args() == [
        {"parameter": "--check-int", "help": "integer help", "type": "int", "required": True},
        {"parameter": "--check-string", "help": "string help", "type": "str", "required": False},
        {"parameter": "--check-bool", "help": "bool help and required is not mentioned", "type": "bool"},
        {"parameter": "--check-float", "help": "float help and required is not mentioned", "type": "float"},
        {"parameter": "--check-json", "help": "json help", "type": "json"},
        {"parameter": "--check-dict", "help": "dict help", "type": "dict"},
        {"parameter": "--check-tuple", "help": "tuple help", "type": "tuple"},
        {"parameter": "--check-list", "help": "list help", "type": "list"},
    ])


def test_function():
    """
    Test when the functionality when the argparse is present inside another function
    """
    file_path = "tests/files/function_test.py"
    e = ExtractArgs(file_path)

    assert (e.find_args() == [
        {"parameter": "--check-int", "help": "integer help", "type": "int", "required": True},
        {"parameter": "--check-string", "help": "string help", "type": "str", "required": False},
        {"parameter": "--check-bool", "help": "bool help and required is not mentioned", "type": "bool"},
        {"parameter": "--check-float", "help": "float help and required is not mentioned", "type": "float"},
        {"parameter": "--check-json", "help": "json help", "type": "json"},
        {"parameter": "--check-dict", "help": "dict help", "type": "dict"},
        {"parameter": "--check-tuple", "help": "tuple help", "type": "tuple"},
        {"parameter": "--check-list", "help": "list help", "type": "list"},
    ])

def test_choices():
    """
    Test if the choices are valid
    """
    file_path = "tests/files/choices_test.py"
    e = ExtractArgs(file_path)

    assert(e.find_args() == [
        {"parameter": "--check-choices", "help": "string help", "type": "str", "required": True,
         "choices": ['rock', 'paper', 'scissors']},
        {"parameter": "--check-range", "type": "int", "choices": {"func_type": "range", "values": (1, 4)}},
    ])