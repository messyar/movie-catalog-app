import logging
from pathlib import Path

from pydantic import BaseModel, ValidationError

from schemas.movie import Movie, MoviesList

BASE_PATH = Path(__file__).parent.parent

logger = logging.getLogger(__name__)

store_path = BASE_PATH / "store.json"
if not store_path.exists():
    with open(store_path, "w") as f:
        f.write(MoviesList.model_validate({}).model_dump_json())


def get_movies_data() -> str:
    with open(store_path, "r") as f_read:
        movie_data = f_read.read()
    return movie_data


class MovieStore(BaseModel):

    def save(
        self,
        movies: dict[str, Movie],
    ) -> None:
        with open(store_path, "w") as data_file:
            data_file.write(MoviesList(movies=movies).model_dump_json())

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
