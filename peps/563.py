from __future__ import annotations


def f(foo: str) -> int:
    ...


def a(kek: str) -> None:
    ...


print(a.__annotations__)
