import datetime


def tricky_function():
    now = datetime.datetime.now()

    return now.year if now.year % 2 else None


class TrickyClass:
    def __init__(self) -> None:
        self.data = tricky_function()

    def get_data(self):
        return -1 if self.data is None else self.data
