import logging
from typing import Annotated

from fastapi import (
    HTTPException,
    BackgroundTasks,
    Request,
    status,
    Depends,
)
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from api.api_v1.movies.crud import storage
from core.config import API_TOKENS
from schemas.movie import Movie

log = logging.getLogger(__name__)

static_api_token = HTTPBearer(
    scheme_name="Static API token",
    description="Your **Static API token** from developer portal. [Read more](#)",
    auto_error=False,
)

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


def check_api_token_for_unsafe_methods(
    request: Request,
    api_token: Annotated[
        HTTPAuthorizationCredentials | None,
        Depends(static_api_token),
    ] = None,
):
    if request.method not in UNSAFE_METHODS:
        return

    if not api_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API token is required",
        )

    if api_token.credentials not in API_TOKENS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API token",
        )
