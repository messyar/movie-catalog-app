from typing import Annotated

from fastapi import Depends, APIRouter

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


@router.get("/{movie_id}", response_model=Movie)
def get_movie(
    movie: Annotated[Movie, Depends(get_movie_by_id)],
):
    return movie
