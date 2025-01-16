from fastapi import Request, Depends
import jwt

from app.config import settings
from app.exceptions import TokenAbsentException, IncorrectTokenFormatException

from app.exceptions import UserIsNotPresentException
from app.users.dao import UsersDAO


def get_token(request: Request):
    token = request.cookies.get("user_access_token")
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except jwt.PyJWTError:
        raise IncorrectTokenFormatException

    tg_id: str = payload.get("sub")
    if not tg_id:
        raise UserIsNotPresentException

    user = await UsersDAO.find_one_or_none(tg_id=int(tg_id))
    if not user:
        raise UserIsNotPresentException

    return user.id

