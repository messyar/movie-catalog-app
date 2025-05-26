from schemas.movie import Movie

MOVIE_LIST = [
    Movie(
        slug="snatch-2001",
        name="Snatch",
        description="""A thief who steals items.""",
        year=2001,
        rating=9.0,
        age_limit=18,
    ),
    Movie(
        slug="brilliantovaya-ruka-1980",
        name="Бриллиантовая рука",
        description="Упал, очнулся - гипс с бриллиантами.",
        year=1980,
        rating=10.0,
        age_limit=12,
    ),
    Movie(
        slug="matrix-1999",
        name="Матрица",
        description="Мы все живем в матрице.",
        year=1999,
        rating=9.5,
        age_limit=16,
    ),
]
