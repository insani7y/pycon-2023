import typing

CustomInt: typing.TypeAlias = int
CustomStr: typing.TypeAlias = str


def foo() -> MyType:
    ...


a: CustomInt = 5
T = typing.TypeVar("T", CustomInt, CustomStr)


class Kek(typing.Generic[T]):
    def sos(self: typing.Self, a: T) -> T:
        return a


Kek[CustomInt]().sos(bool)
