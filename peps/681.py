import typing


# The ``ModelMeta`` metaclass and ``ModelBase`` class are defined by
# a library. This could be in a type stub or inline.
# The ``ModelBase`` class is defined by a library. This could be in
# a type stub or inline.
@typing.dataclass_transform()
class ModelBase:
    ...


# The ``ModelBase`` class can now be used to create new model
# subclasses, like this:
class CustomerModel(ModelBase):
    id: int
    name: str


# Using positional arguments
c1 = CustomerModel(327, "John Smith")

# Using keyword arguments
c2 = CustomerModel(id=327, name="John Smith")

# These calls will generate runtime errors and should be flagged as
# errors by a static type checker.
c3 = CustomerModel()
c4 = CustomerModel(327, first_name="John")
c5 = CustomerModel(327, "John Smith", 0)
