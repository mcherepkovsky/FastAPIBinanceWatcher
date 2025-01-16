from fastapi import APIRouter, Response, Depends

# from app.exceptions import UserAlreadyExistsException, IncorrectEmailOrPasswordException
from app.users.auth import create_access_token
from app.users.dao import UsersDAO
#from app.users.dependences import get_current_user, get_current_admin_user
from app.users.models import Users
from app.users.schemas import TelegramAuthData

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"]
)


@router.post("/telegram")
async def telegram_auth(response: Response, tg_data: TelegramAuthData):
    existing_user = await UsersDAO.find_one_or_none(tg_id=tg_data.id)

    if not existing_user:
        await UsersDAO.add(tg_id=tg_data.id, username=tg_data.username)

    access_token = create_access_token({"sub": str(tg_data.id)})
    response.set_cookie("user_access_token", access_token, httponly=True)

    return {"id": tg_data.id, "username": tg_data.username, "first_name": tg_data.first_name}

# @router.post("/register")
# async def register_user(user_data: SUserAuth):
#     existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
#     if existing_user:
#         raise UserAlreadyExistsException
#     hashed_password = get_password_hash(user_data.password)
#     await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)


# @router.post("/login")
# async def login_user(response: Response, user_data: SUserAuth):
#     # user = await authenticate_user(user_data.email, user_data.password)
#     # if not user:
#     #     raise IncorrectEmailOrPasswordException
#     # access_token = create_access_token({"sub": str(user.id)})
#     # response.set_cookie("booking_access_token", access_token, httponly=True)
#     # return access_token

#
# @router.get("/me")
# async def read_users_me(current_user: Users = Depends(get_current_user)):
#     return current_user
#
#
# @router.get("/all")
# async def read_users_all(current_user: Users = Depends(get_current_admin_user)):
#     return await UsersDAO.find_all()
