from fastapi import APIRouter, status, BackgroundTasks
from fastapi.params import Depends

from api.api_v1.movies.crud import storage
from api.api_v1.movies.dependencies import save_storage
from api.api_v1.movies.helpers.slug_helper import create_slug
from schemas.movie import (
    Movie,
    MovieCreate,
    MovieRead,
)

router = APIRouter(
    prefix="/movies",
    tags=["Movies"],
)

save_router = APIRouter(
    dependencies=[Depends(save_storage)],
)


@router.get(
    "/",
    response_model=list[MovieRead],
)
def get_movies() -> list[Movie]:
    return storage.get()


@save_router.post(
    "/",
    response_model=MovieRead,
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


router.include_router(
    save_router,
)
