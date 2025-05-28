from typing import Annotated

from annotated_types import Len, Interval, MaxLen
from pydantic import BaseModel


class MovieBase(BaseModel):
    name: Annotated[
        str,
        Len(1, 250),
    ]
    description: Annotated[
        str,
        MaxLen(250),
    ] = ""


class MovieExtended(MovieBase):
    """Модель с дополнительными полями"""

    year: Annotated[
        int,
        Interval(ge=1895),  # 1895 is the year of the first movie
    ]
    rating: Annotated[
        float,
        Interval(ge=1, le=10),
    ]
    age_limit: Annotated[
        int,
        Interval(ge=0, le=18),
    ]


class Movie(MovieExtended):
    slug: str


class MovieCreate(MovieExtended):
    """Модель для создания фильма"""


class MovieUpdate(MovieExtended):
    """Модель для обновления фильма"""

    description: Annotated[
        str,
        MaxLen(250),
    ]
