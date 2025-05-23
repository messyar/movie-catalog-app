from typing import Annotated

from fastapi import FastAPI, Request, status, Depends, Response
from fastapi.exceptions import HTTPException

from schemas.movie import Movie

app = FastAPI(
    title="Movie Catalog",
)


@app.get("/")
def read_root(
    request: Request,
    name: str = "Anonym",
):
    docs_url = request.url.replace(
        path="/docs",
        query="",
    )
    return {
        "message": f"{name}, welcome to Movie Catalog app!",
        "docs": str(docs_url),
    }


MOVIE_LIST = [
    Movie(
        id=1,
        name="Snatch",
        description="""A thief who steals items.""",
        year=2001,
        rating=9.0,
        age_limit=18,
    ),
    Movie(
        id=2,
        name="Бриллиантовая рука",
        description="Упал, очнулся - гипс с бриллиантами.",
        year=1980,
        rating=10.0,
        age_limit=12,
    ),
    Movie(
        id=3,
        name="Матрица",
        description="Мы все живем в матрице.",
        year=2002,
        rating=9.5,
        age_limit=16,
    ),
]


def get_movie_by_id(
    movie_id: int,
):
    movie: Movie | None = next(
        (movie for movie in MOVIE_LIST if movie.id == movie_id),
        None,
    )
    if movie:
        return movie
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Movie with id {movie_id} not found",
    )


@app.get(
    "/movie",
    response_model=list[Movie],
)
def get_movies():
    return MOVIE_LIST


@app.get("/movie/{movie_id}", response_model=Movie)
def get_movie(
    movie: Annotated[Movie, Depends(get_movie_by_id)],
):
    return movie
