import dataclasses
import typing


def magic_get(obj: typing.Any, attr: str) -> typing.Any:
    """Dynamically gets an attribute from an object."""
    return getattr(obj, attr)


@dataclasses.dataclass
class SomeClass:
    attribute: int
    custom_attribute: "SomeClass" | None = None


obj = SomeClass(1, SomeClass(1))


# Revealed type is "builtins.int"
reveal_type(magic_get(obj, "attribute"))

# Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
attribute: str = magic_get(obj, "attribute")

# Revealed type is "Union[mypy_directory.magic.SomeClass, None]"
reveal_type(magic_get(obj, "custom_attribute"))

# "SomeClass" has no attribute "attribute_2"; maybe "attribute"?  [attr-defined]
# Revealed type is Any
reveal_type(magic_get(obj, "attribute_2"))
