import random
from typing import Annotated

from fastapi import Depends, APIRouter, status

from .crud import MOVIE_LIST
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
def get_movies():
    return MOVIE_LIST


@router.post(
    "/",
    response_model=Movie,
    status_code=status.HTTP_201_CREATED,
)
def create_movie(
    movie_create: MovieCreate,
):
    return Movie(
        slug=create_slug(
            name_in=movie_create.name,
            year=movie_create.year,
        ),
        **movie_create.model_dump(),
    )


@router.get("/{movie_id}", response_model=Movie)
def get_movie(
    movie: Annotated[Movie, Depends(get_movie_by_slug)],
):
    return movie
