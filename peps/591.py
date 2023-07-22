import typing


@typing.final
class Base:
    ...


class Derived(Base):  # Error: Cannot inherit from final class "Base"
    ...


from typing import final


class Base2:
    @final
    def __foo(self) -> None:
        ...


class Derived2(Base2):
    def __foo(self) -> None:
        ...


ID: typing.Final[float] = 1

ID = 2
