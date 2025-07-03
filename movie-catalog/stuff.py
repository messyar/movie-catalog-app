from redis import Redis
from core import config

redis = Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    db=config.REDIS_DB,
    decode_responses=True,
)


def main():
    print(redis.ping())
    redis.set("name", "John")
    redis.set("foo", "bar")
    redis.set("number", "42")
    for key in redis.keys():
        print(redis.get(key))

    print(redis.get("spam"))
    print(redis.getdel("name"))
    print(redis.get("name"))


if __name__ == "__main__":
    main()
