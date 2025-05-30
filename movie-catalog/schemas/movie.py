from typing import Annotated

from annotated_types import Len, Interval, MaxLen
from pydantic import BaseModel


NameString = Annotated[
    str,
    Len(1, 250),
]

DescriptionString = Annotated[
    str,
    MaxLen(250),
]

YearString = Annotated[
    int,
    Interval(ge=1895),  # 1895 is the year of the first movie
]

RatingString = Annotated[
    float,
    Interval(ge=1, le=10),
]

AgeLimitString = Annotated[
    int,
    Interval(ge=0, le=18),
]


class MovieBase(BaseModel):
    name: NameString
    description: DescriptionString = ""


class MovieExtended(MovieBase):
    """Модель с дополнительными полями"""

    year: YearString
    rating: RatingString
    age_limit: AgeLimitString


class Movie(MovieExtended):
    slug: str
    notes: str = ""


class MovieRead(MovieExtended):
    """Модель для чтения информации о фильме"""

    slug: str


class MovieCreate(MovieExtended):
    """Модель для создания фильма"""


class MovieUpdate(MovieExtended):
    """Модель для обновления фильма"""

    description: DescriptionString


class MovieUpdatePartial(MovieExtended):
    """Модель для частичного обновления фильма"""

    name: NameString | None = None
    description: DescriptionString | None = None
    year: YearString | None = None
    rating: RatingString | None = None
    age_limit: AgeLimitString | None = None
