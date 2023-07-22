import typing


class Shape:
    def set_scale(self: typing.Self, scale: float) -> typing.Self:
        self.scale = scale
        return self


class Circle(Shape):
    def set_radius(self: typing.Self, radius: float) -> typing.Self:
        self.radius = radius
        return self
