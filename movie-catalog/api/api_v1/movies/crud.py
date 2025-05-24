from schemas.movie import Movie

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
