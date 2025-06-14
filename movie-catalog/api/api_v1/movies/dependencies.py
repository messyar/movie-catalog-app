import logging

from fastapi import (
    HTTPException,
    BackgroundTasks,
    Request,
    status,
)

from api.api_v1.movies.crud import storage
from schemas.movie import Movie

log = logging.getLogger(__name__)

UNSAFE_METHODS = frozenset(
    {
        "POST",
        "DELETE",
        "PATCH",
        "PUT",
    }
)


def get_movie_by_slug(
    slug: str,
):
    movie: Movie | None = storage.get_by_slug(slug=slug)
    if movie:
        return movie
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Movie with slug {slug} not found",
    )


def save_storage(
    request: Request,
    background_task: BackgroundTasks,
):
    yield
    if request.method in UNSAFE_METHODS:
        log.info("Background task to save to storage added")
        background_task.add_task(storage.save_to_store)
