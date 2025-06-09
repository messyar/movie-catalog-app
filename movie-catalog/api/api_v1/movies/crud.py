from pydantic import BaseModel

from schemas.movie import (
    Movie,
    MovieUpdate,
    MovieUpdatePartial,
)
from store.movies.movie_store import MovieStore


class MovieCrud(BaseModel):
    movie_store: MovieStore = MovieStore()

    def get(self) -> list[Movie]:
        return list(self.movie_store.get_movies().values())

    def get_by_slug(self, slug: str) -> Movie | None:
        return self.movie_store.get_movie_by_slug(slug)

    def create(self, movie_in: Movie) -> Movie:
        return self.movie_store.create_movie(movie_in=movie_in)

    def delete_by_slug(self, slug: str) -> None:
        self.movie_store.delete_movie_by_slug(slug=slug)

    def delete(self, movie_in: Movie) -> None:
        self.delete_by_slug(slug=movie_in.slug)

    def update(
        self,
        movie: Movie,
        movie_in: MovieUpdate,
    ) -> Movie:
        for field_name, value in movie_in:
            setattr(movie, field_name, value)
        self.movie_store.update_movie(movie=movie)
        return movie

    def update_partial(
        self,
        movie: Movie,
        movie_in: MovieUpdatePartial,
    ) -> Movie:
        for field_name, value in movie_in.model_dump(exclude_unset=True).items():
            setattr(movie, field_name, value)
        self.movie_store.update_movie(movie=movie)
        return movie


storage = MovieCrud()
