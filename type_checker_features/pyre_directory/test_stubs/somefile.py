"""Some help text."""
import dataclasses


@dataclasses.dataclass(order=True)
class Window:
    width: int
    height: int

    def area(self) -> int:
        return self.width * self.height


def create_empty() -> Window:
    return Window(0, 0)
