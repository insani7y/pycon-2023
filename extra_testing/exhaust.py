from enum import Enum
from typing import Literal, NoReturn

PossibleValues = Literal["one", "two"]


def assert_never(value: NoReturn) -> NoReturn:
    # This also works at runtime as well
    assert False, f"This code should never be reached, got: {value}"


def validate(x: PossibleValues) -> bool:
    if x in ("one", "two"):
        return True
    assert_never(x)


class Milk(Enum):
    cow = "Cow"
    almond = "Almond"
    cashew = "Cashew"
    oat = "Oat"


def portion_ml(milk: Milk) -> int:
    match milk:
        case Milk.cow:
            return 100
        case Milk.almond | Milk.cashew | Milk.oat:
            return 120
        case _ as unreachable:
            assert_never(unreachable)
