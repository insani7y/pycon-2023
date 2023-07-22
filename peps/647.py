import typing


def func1(val: str | None):
    # "is None" type guard
    if val is not None:
        print(val)
        val.
    else:
        val.
        print(val)


def func2(val: str | None):
    # Truthy type guard
    if val:
        val.
        print(val)
    else:
        val.
        print(val)

def func2(val: str | None):
    # Truthy type guard
    if isinstance(val, str):
        print(val)
    else:
        print(val)

def func3(val: str | float):
    # "isinstance" type guard
    if isinstance(val, str):
        reveal_type(val)
    else:
        reveal_type(val)


def func4(val: typing.Literal[1, 2]):
    # Comparison type guard
    if val == 1:
        reveal_type(val)
    else:
        reveal_type(val)
