# This sample tests handling of the Python 3.9 "Annotated" feature
# described in PEP 593.

from typing import Annotated


class struct2:
    @staticmethod
    def ctype(a: str):
        pass

    class Packed:
        pass


UnsignedShort = Annotated[int, struct2.ctype("H")]
SignedChar = Annotated[int, struct2.ctype("b")]


class Student(struct2.Packed):
    name: Annotated[str, struct2.ctype("<10s")]
    serialnum: UnsignedShort
    school: SignedChar


def ValueRange(a: int, b: int):
    pass


T1 = Annotated[int, ValueRange(-10, 5)]
T2 = Annotated[T1, ValueRange(-20, 3)]

a: Annotated[Annotated[int]] = 3
b: T2 = 5


T3 = Annotated[str, int]
T4 = Annotated[int, int]

c: T3 = "asdf"
d: T4 = "asdf"


def kek(a: T3) -> None:
    return None


kek(c)
kek(d)
