from fastapi import APIRouter
from .movies.views import router as movie_views


router = APIRouter(
    prefix="/v1",
)
router.include_router(movie_views)
