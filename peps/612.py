import typing

P = typing.ParamSpec("P")
R = typing.TypeVar("R")


def add_logging(f: typing.Callable[P, R]) -> typing.Callable[P, R]:
    def inner(*args: P.args, **kwargs: P.kwargs) -> R:
        return f(*args, **kwargs)

    return inner


@add_logging
def takes_int_str(x: int, y: str) -> int:
    return x + 7


@add_logging
def takes_str(s: str) -> str:
    return s


takes_int_str(1, "A")  # Accepted
takes_int_str("B", 2)  # Correctly rejected by the type checker


def expects_int_first(x: typing.Callable[typing.Concatenate[int, P], int]) -> None: ...


@expects_int_first # Rejected
def one(x: str) -> int: ...


@expects_int_first # Rejected
def two(*, x: int) -> int: ...


@expects_int_first # Rejected
def three(**kwargs: int) -> int: ...


@expects_int_first # Accepted
def four(*args: int) -> int: ...
