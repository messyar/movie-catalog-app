import logging

from fastapi import HTTPException, BackgroundTasks
from starlette import status

from api.api_v1.movies.crud import storage
from schemas.movie import Movie

log = logging.getLogger(__name__)


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
    background_task: BackgroundTasks,
):
    yield
    log.info("Background task to save to storage added")
    background_task.add_task(storage.save_to_store)
