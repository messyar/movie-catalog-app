import random
from typing import Annotated

from fastapi import Depends, APIRouter, status

from .crud import storage
from .dependencies import get_movie_by_slug
from .helpers.slug_helper import create_slug
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


@router.get("/{slug}", response_model=Movie)
def get_movie(
    movie: Annotated[Movie, Depends(get_movie_by_slug)],
) -> Movie:
    return movie


@router.delete(
    "/{slug}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Movie not found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Movie with 'slug' not found",
                    }
                }
            },
        },
    },
)
def delete_movie(
    movie: Annotated[
        Movie,
        Depends(get_movie_by_slug),
    ],
) -> None:
    storage.delete(movie_in=movie)
