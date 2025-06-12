from typing import Annotated

from fastapi import APIRouter, Depends, BackgroundTasks
from starlette import status

from api.api_v1.movies.crud import storage
from api.api_v1.movies.dependencies import get_movie_by_slug
from schemas.movie import (
    Movie,
    MovieUpdate,
    MovieUpdatePartial,
    MovieRead,
)

router = APIRouter(
    prefix="/{slug}",
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


MovieBySlug = Annotated[
    Movie,
    Depends(get_movie_by_slug),
]


@router.get(
    "/",
    response_model=MovieRead,
)
def get_movie(
    movie: MovieBySlug,
) -> Movie:
    return movie


@router.put(
    "/",
    response_model=MovieRead,
)
def update_movie_details(
    movie: MovieBySlug,
    movie_in: MovieUpdate,
    background_tasks: BackgroundTasks,
) -> Movie:
    background_tasks.add_task(storage.save_to_store)
    return storage.update(movie=movie, movie_in=movie_in)


@router.patch(
    "/",
    response_model=MovieRead,
)
def update_movie_details_partial(
    movie: MovieBySlug,
    movie_in: MovieUpdatePartial,
    background_tasks: BackgroundTasks,
) -> Movie:
    background_tasks.add_task(storage.save_to_store)
    return storage.update_partial(movie=movie, movie_in=movie_in)


@router.delete(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_movie(
    movie: MovieBySlug,
    background_tasks: BackgroundTasks,
) -> None:
    background_tasks.add_task(storage.save_to_store)
    storage.delete(movie_in=movie)
