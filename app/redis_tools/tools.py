import redis.asyncio as redis

from app.config import settings


class RedisTools:
    r = redis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}")

    @classmethod
    async def set_all_pairs(cls, pairs: dict):
        await cls.r.delete("pairs")
        await cls.r.hset("pairs", mapping=pairs)

    @classmethod
    async def set_pair(cls, pair: str, price: str):
        await cls.r.hset("pairs", pair, price)

    @classmethod
    async def get_pair(cls, pair: str):
        return await cls.r.hget("pairs", pair)

    @classmethod
    async def get_all_pairs(cls):
        return await cls.r.hgetall("pairs")

    @classmethod
    async def set_popular_pairs(cls, pairs: str):
        return await cls.r.set("popular_pairs", pairs)

    @classmethod
    async def get_popular_pairs(cls):
        return await cls.r.get("popular_pairs")
