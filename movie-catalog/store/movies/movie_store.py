import logging

from pydantic import BaseModel, ValidationError

from schemas.movie import Movie, MoviesList
from core.config import store_path


logger = logging.getLogger(__name__)


def get_movies_data() -> str:
    if not store_path.exists():
        store_path.write_text(MoviesList(movies={}).model_dump_json())
    return store_path.read_text()


class MovieStore(BaseModel):

    def save(
        self,
        movies: dict[str, Movie],
    ) -> None:
        store_path.write_text(MoviesList(movies=movies).model_dump_json(indent=2))

    def get_movies(
        self,
    ) -> dict[str, Movie]:
        try:
            return MoviesList.model_validate_json(get_movies_data()).movies
        except ValidationError as exc:
            logger.error("Failed to validate movies: %s", exc)
        return {}

    def get_movie_by_slug(
        self,
        slug: str,
    ) -> Movie | None:
        return self.get_movies().get(slug)

    def create_movie(
        self,
        movie_in: Movie,
    ) -> Movie:
        movies = self.get_movies()
        logger.info("Movies: %s", movies)
        movies[movie_in.slug] = movie_in
        self.save(movies=movies)
        return movie_in

    def delete_movie_by_slug(
        self,
        slug: str,
    ) -> None:
        movies = self.get_movies()

        movies.pop(slug, None)
        self.save(movies=movies)

    def update_movie(
        self,
        movie: Movie,
    ) -> Movie:
        movies = self.get_movies()
        movies[movie.slug] = movie
        self.save(movies=movies)
        return movie
