#   Primary Author: Aadesh M Bagmar <aadeshbagmar@gmail..com>
#
#   Purpose: Adding support for all the functions. Each function should have a standard
#   format where it starts with prefix check_, accepts the value node from ast.Call and returns a
#   dictionary with keys "func_type" and "values". Please add
#   corresponding support to the validator.

import ast
from typing import Dict, Union

def check_function(parsed_value_arg: ast.Call)->Union[str, Dict]:
    """
    Function to verify a function

    Args:
        parsed_value_arg: Parser value object from function call

    Returns:
        Dictionary defining the function type and the value. In case it matches no function that has been mentioned,
        return "Unknown Type"
    """
    if parsed_value_arg.func.id == "range":
        return {"func_type": "range", "values": [parsed_value_arg.args[0].n, parsed_value_arg.args[1].n]}
    else:
        return "Unknown Type"