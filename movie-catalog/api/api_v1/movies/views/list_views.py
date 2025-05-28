from fastapi import APIRouter, status

from api.api_v1.movies.crud import storage
from api.api_v1.movies.helpers.slug_helper import create_slug
from schemas.movie import Movie, MovieCreate

router = APIRouter(
    prefix="/movies",
    tags=["Movies"],
)


@router.get(
    "/",
    response_model=list[Movie],
)
def get_movies() -> list[Movie]:
    return storage.get()


@router.post(
    "/",
    response_model=Movie,
    status_code=status.HTTP_201_CREATED,
)
def create_movie(
    movie_create: MovieCreate,
) -> Movie:
    return storage.create(
        Movie(
            slug=create_slug(
                name_in=movie_create.name,
                year=movie_create.year,
            ),
            **movie_create.model_dump(),
        )
    )
