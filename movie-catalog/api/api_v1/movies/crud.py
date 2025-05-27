from pydantic import BaseModel

from schemas.movie import (
    Movie,
    MovieCreate,
)


class MovieStorage(BaseModel):
    movie_info: dict[str, Movie] = {}

    def get(self) -> list[Movie]:
        return list(self.movie_info.values())

    def get_by_slug(self, slug: str) -> Movie | None:
        return self.movie_info.get(slug)

    def create(self, movie_in: Movie) -> Movie:
        self.movie_info[movie_in.slug] = movie_in
        return movie_in


storage = MovieStorage()

storage.create(
    Movie(
        slug="snatch-2001",
        name="Snatch",
        description="""A thief who steals items.""",
        year=2001,
        rating=9.0,
        age_limit=18,
    )
)

storage.create(
    Movie(
        slug="brilliantovaya-ruka-1980",
        name="Бриллиантовая рука",
        description="Упал, очнулся - гипс с бриллиантами.",
        year=1980,
        rating=10.0,
        age_limit=12,
    ),
)

storage.create(
    Movie(
        slug="matrix-1999",
        name="Матрица",
        description="Мы все живем в матрице.",
        year=1999,
        rating=9.5,
        age_limit=16,
    ),
)
