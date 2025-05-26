from typing import Annotated

from annotated_types import Len, Interval
from pydantic import BaseModel


class MovieBase(BaseModel):
    name: str
    description: str


class MovieCreate(MovieBase):
    name: Annotated[
        str,
        Len(5, 150),
    ]
    description: Annotated[
        str,
        Len(10, 250),
    ]
    year: Annotated[
        int,
        Interval(ge=1895),  # 1895 is the year of the first movie
    ]
    rating: Annotated[
        int,
        Interval(ge=1, le=10),
    ]
    age_limit: Annotated[
        int,
        Interval(ge=0, le=18),
    ]


class Movie(MovieBase):
    id: int
    year: int
    rating: float
    age_limit: int
