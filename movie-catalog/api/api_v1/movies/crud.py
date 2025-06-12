import logging

from pydantic import BaseModel, ValidationError

from core.config import STORE_PATH
from schemas.movie import (
    Movie,
    MovieUpdate,
    MovieUpdatePartial,
)

log = logging.getLogger(__name__)


class MovieCrud(BaseModel):
    movies: dict[str, Movie] = {}

    def save_to_store(self) -> None:
        STORE_PATH.write_text(self.model_dump_json(indent=2))
        log.info("Movie saved to store successfully")

    @classmethod
    def from_store(cls) -> "MovieCrud":
        if not STORE_PATH.exists():
            log.info("Movie storage file does not exist.")
            return cls()
        return cls.model_validate_json(STORE_PATH.read_text())

    def init_store(self) -> None:
        try:
            data = MovieCrud.from_store()
        except ValidationError:
            self.save_to_store()
            log.warning("Rewriting movie storage file due to validation error")
            return

        self.movies.update(
            data.movies,
        )
        log.warning("Recovered data from movie storage file")

    def get(self) -> list[Movie]:
        return list(self.movies.values())

    def get_by_slug(self, slug: str) -> Movie | None:
        return self.movies.get(slug)

    def create(self, movie_in: Movie) -> Movie:
        self.movies[movie_in.slug] = movie_in
        self.save_to_store()
        log.info("Movie created successfully")
        return movie_in

    def delete_by_slug(self, slug: str) -> None:
        self.movies.pop(slug)
        self.save_to_store()

    def delete(self, movie_in: Movie) -> None:
        self.delete_by_slug(slug=movie_in.slug)

    def update(
        self,
        movie: Movie,
        movie_in: MovieUpdate,
    ) -> Movie:
        for field_name, value in movie_in:
            setattr(movie, field_name, value)
        self.save_to_store()
        return movie

    def update_partial(
        self,
        movie: Movie,
        movie_in: MovieUpdatePartial,
    ) -> Movie:
        for field_name, value in movie_in.model_dump(exclude_unset=True).items():
            setattr(movie, field_name, value)
        self.save_to_store()
        return movie


storage = MovieCrud()
