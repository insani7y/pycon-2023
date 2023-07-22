import datetime
from typing import Optional


def tricky_function() -> Optional[int]:
    now = datetime.datetime.now()

    if now.year % 2:
        return now.year

    return None


class TrickyClass:
    def __init__(self) -> None:
        self.data = tricky_function()

    def get_data(self):
        if self.data is None:
            return -1

        return self.data
