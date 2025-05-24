from typing import Annotated

from fastapi import FastAPI, Request, Depends

from api.api_v1.movies.crud import MOVIE_LIST
from api.api_v1.movies.dependencies import get_movie_by_id
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
