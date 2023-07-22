import typing


class SupportsClose(typing.Protocol):
    def close(self) -> None:
        ...


class Resource:
    ...

    def close(self) -> None:
        print("closed")


def some_function(closer: SupportsClose) -> None:
    closer.close()


resource: Resource = Resource()
some_function(resource)
