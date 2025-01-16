from pydantic import HttpUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: int

    CURRENCY_PAIR_KEY: HttpUrl
    ALL_PAIRS_KEY: HttpUrl
    BINANCE_API_URL: HttpUrl

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    SECRET_KEY: str
    ALGORITHM: str

    TG_BOT_TOKEN: str

    class Config:
        env_file = ".env"


settings = Settings()
