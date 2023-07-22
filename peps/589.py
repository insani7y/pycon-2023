from typing import TypedDict


class Movie2(TypedDict):
    name: str
    year: int


class Movie(TypedDict):
    name: str
    year: int
    movie: Movie2


movie: Movie = {"name": "Blade Runner", "year": 1982, "movie": {"name": "Blade Runner", "year": 1982}}
