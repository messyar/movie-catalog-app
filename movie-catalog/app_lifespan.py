from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.api_v1.movies.crud import storage


@asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    # Действия до запуска приложения
    storage.init_store()
    # Ставим функцию на паузу
    yield
    # Действия при завершении работы приложения
