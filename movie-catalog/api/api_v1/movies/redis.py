import secrets
from abc import ABC, abstractmethod

from redis import Redis
from core import config


class AbstractTokensHelper(ABC):
    """
    Что нужно от обертки:
    - Проверка токена
    - Добавление токена
    - Генерация и добавление токена
    """

    @abstractmethod
    def token_exists(self, token: str) -> bool:
        """
        Check if token exists.
        :param token:
        :return:
        """

    @abstractmethod
    def add_token(self, token: str) -> None:
        """
        Save token to storage.
        :param token:
        :return:
        """

    def generate_and_add_token(self) -> str:
        token = secrets.token_urlsafe(config.TOKEN_LENGTH)
        self.add_token(token)
        return token


class RedisTokensHelper(AbstractTokensHelper):

    def __init__(
        self,
        host: str,
        port: int,
        db: int,
        tokens_set_name: str,
    ):
        self.redis = Redis(
            host=host,
            port=port,
            db=db,
            decode_responses=True,
        )
        self.tokens_set_name = tokens_set_name

    def add_token(self, token: str) -> None:
        self.redis.sadd(self.tokens_set_name, token)

    def token_exists(self, token: str) -> bool:
        return bool(
            self.redis.sismember(
                self.tokens_set_name,
                token,
            )
        )


redis_tokens = RedisTokensHelper(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    db=config.REDIS_DB_TOKENS,
    tokens_set_name=config.REDIS_TOKENS_SET_NAME,
)
