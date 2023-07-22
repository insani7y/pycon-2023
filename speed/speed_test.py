import os
import timeit

initial_command: str  # input your base command here


def get_command(initial_command: str, project: str) -> str:
    return f"{initial_command} speed/{project}"


lines_10k: float = timeit.timeit(lambda: os.system(get_command(initial_command, "10k-lines")), number=30) / 30
lines_15k: float = timeit.timeit(lambda: os.system(get_command(initial_command, "15k-lines")), number=30) / 30
lines_25k: float = timeit.timeit(lambda: os.system(get_command(initial_command, "25k-lines")), number=30) / 30
lines_35k: float = timeit.timeit(lambda: os.system(get_command(initial_command, "35k-lines")), number=30) / 30

print(f"{lines_10k=}, {lines_15k=}, {lines_25k=}, {lines_35k=}")
