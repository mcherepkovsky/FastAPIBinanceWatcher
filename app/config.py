from pydantic import HttpUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: int

    CURRENCY_PAIR_KEY: HttpUrl
    ALL_PAIRS_KEY: HttpUrl
    BINANCE_API_URL: HttpUrl

    class Config:
        env_file = ".env"


settings = Settings()
