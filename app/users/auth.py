import jwt

from app.config import settings


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    encode_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, settings.ALGORITHM
    )
    return encode_jwt
