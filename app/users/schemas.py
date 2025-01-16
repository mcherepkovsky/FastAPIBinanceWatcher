from pydantic import BaseModel


class TelegramAuthData(BaseModel):
    id: int
    first_name: str
    username: str = None
    photo_url: str
    auth_date: int
    hash: str
