from pydantic import BaseModel

from schemas.movie import (
    Movie,
    MovieUpdate,
    MovieUpdatePartial,
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

    def delete_by_slug(self, slug: str) -> None:
        self.movie_info.pop(slug, None)

    def delete(self, movie_in: Movie) -> None:
        self.delete_by_slug(slug=movie_in.slug)

    def update(
        self,
        movie: Movie,
        movie_in: MovieUpdate,
    ) -> Movie:
        for field_name, value in movie_in:
            setattr(movie, field_name, value)
        return movie

    def update_partial(
        self,
        movie: Movie,
        movie_in: MovieUpdatePartial,
    ) -> Movie:
        for field_name, value in movie_in.model_dump(exclude_unset=True).items():
            setattr(movie, field_name, value)
        return movie


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
