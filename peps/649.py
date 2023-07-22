import typing


def make_func(val: int | None) -> typing.Callable[[], None | int]:
    if val is None:
        def kek() -> None:
            print(None)
        return kek
    else:
        def kek2() -> int:
            return val
        return kek2


# Usage:
f1 = make_func(None)
f2 = make_func(1)

val1 = f1()