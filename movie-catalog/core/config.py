import logging
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent.parent
STORE_PATH = BASE_PATH / "store.json"


LOG_LEVEL = logging.INFO
LOG_FORMAT: str = (
    "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"
)

# Only for demo!
# no real users in code!!
USERS_DB: dict[str, str] = {
    # "username": "password"
    "sam": "password",
    "bob": "qwerty",
}


REDIS_HOST: str = "localhost"
REDIS_PORT: int = 6379
REDIS_DB: int = 0
REDIS_DB_TOKENS: int = 1

REDIS_TOKENS_SET_NAME: str = "tokens"
