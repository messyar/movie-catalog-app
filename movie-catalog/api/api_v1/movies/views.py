import datetime
import random
from annotated_types import Len, Interval
from typing import Annotated

from fastapi import Depends, APIRouter, status, Form

from api.api_v1.movies.crud import MOVIE_LIST
from api.api_v1.movies.dependencies import get_movie_by_id
from schemas.movie import Movie

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


def generate_movie_id():
    return random.randint(5, 100)


@router.post(
    "/",
    response_model=Movie,
    status_code=status.HTTP_201_CREATED,
)
def create_movie(
    name: Annotated[str, Len(5, 150), Form()],
    description: Annotated[str, Len(10, 250), Form()],
    year: Annotated[int, Interval(ge=1895), Form()],
    rating: Annotated[int, Interval(ge=1, le=10), Form()],
    age_limit: Annotated[int, Interval(ge=0, le=18), Form()] = 18,
):
    return Movie(
        id=generate_movie_id(),
        name=name,
        description=description,
        year=year,
        rating=rating,
        age_limit=age_limit,
    )


@router.get("/{movie_id}", response_model=Movie)
def get_movie(
    movie: Annotated[Movie, Depends(get_movie_by_id)],
):
    return movie
