import typing


class Movie(typing.TypedDict):
    title: str
    year: typing.NotRequired[int]


movie: Movie = {"title": "title", "year": "year"}
movie2: Movie = {"title": "title"}
movie3: Movie = {"title": "title", "year": 1}
movie10: Movie = {"year": 1}


class Movie2(typing.TypedDict):
    title: str
    year: typing.NotRequired[int]
    movie: typing.NotRequired[Movie]


movie4: Movie2 = {"title": "title", "year": 1}
movie5: Movie2 = {
    "title": "title",
    "year": 1,
    "movie": movie,
}
