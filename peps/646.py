import typing

DType = typing.TypeVar("DType")
Shape = typing.TypeVarTuple("Shape")


class Array(typing.Generic[DType, *Shape]):
    def __abs__(self) -> Array[DType, *Shape]:
        ...

    def __add__(self, other: Array[DType, *Shape]) -> Array[DType, *Shape]:
        ...


Height = typing.NewType("Height", int)
Width = typing.NewType("Width", int)

x: Array[float, Height, Width] = Array()
