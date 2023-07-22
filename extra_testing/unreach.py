def main(argument: int | None) -> int | None:
    if isinstance(argument, int):
        return argument + 1

    if argument is None:
        print("SOS")
        return None

    return 1234
