from pydantic import BaseModel


class MovieBase(BaseModel):
    id: int
    name: str
    description: str


class Movie(MovieBase):
    year: int
    rating: float
    age_limit: int
