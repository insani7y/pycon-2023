def f():
    return "PyCon"


def g():
    return f() + 2019

def f():
    return "PyCon"
def g():
    return f() + 2019

 # pytype: line 4, in g: unsupported operand type(s) for +: 'str'
 # and 'int' [unsupported-operands]

from typing import List
def get_list() -> list[str]:
    lst: list[str] = ["PyCon"]
    lst.append(2019)
    return [str(x) for x in lst]

 # mypy: line 4: error: Argument 1 to "append" of "list" has
 # incompatible type "int"; expected "str"