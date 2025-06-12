import logging

from fastapi import FastAPI, Request
from api import router as api_router
from app_lifespan import lifespan
from core.config import LOG_FORMAT, LOG_LEVEL

logging.basicConfig(
    level=LOG_LEVEL,
    format=LOG_FORMAT,
)

app = FastAPI(
    title="Movie Catalog",
    lifespan=lifespan,
)
app.include_router(api_router)


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
