import functools


class MyClass:
    @property
    def name(self):
        return "MyClass"


functools.lru_cache()
