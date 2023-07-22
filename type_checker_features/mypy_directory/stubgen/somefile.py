"""Some help text."""
import dataclasses


@dataclasses.dataclass(order=True)
class Window:
    width: int
    height: int

    def area(self):
        return self.width * self.height

def create_empty():
    return Window(0, 0)
