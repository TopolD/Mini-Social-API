from fastapi import APIRouter, Response
from fastapi.params import Depends

from app.users.auth import get_password_hash, authenticate_user, create_access_token, create_refresh_token
from app.users.dao import UsersDao
from app.users.dependencies import get_current_user
from app.users.schemas import SUserAuth
from app.users.models import Users
from app.exceptions import IncorrectTokenFormatException, IncorrectEmailOrPasswordException, UserAlreadyExistsException

router = APIRouter(
    prefix="/auth",
    tags=["Auth "]
)


@router.post(
    "/register",
    responses={
        200: {"description": "Зареіструвався"},
        400: {"description": "Невалідні дані"},
        409: {"description": "Такий користувач вже існує"}
    }
)
async def register_user(user_data: SUserAuth):
    """

    :param user_data:
    :return: None
    """

    existing_user = await UsersDao.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException()
    hashed_password = get_password_hash(user_data.password)
    await UsersDao.add(email=user_data.email, hashed_password=hashed_password)





@router.post(
    "/login",
    response_model=str,
    responses={
        200: {"description": "Успішний вхід"},
        # 400: {"description": "Невалідні дані"},
    }
)
async def login_user(response: Response, user_data: SUserAuth) -> str:
    """

    :param response:
    :param user_data:
    :return: access_token
    """

    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException()
    refresh_token = create_refresh_token({"sub": str(user.id)})
    response.set_cookie("token", value=refresh_token, httponly=True, secure=True, samesite="strict")

    access_token = create_access_token({"sub": str(user.id)})

    return access_token


@router.post(
    "/logout",
    responses={
        200: {"description": "Успішний вихід"},
    }
)
def logout_user(
        response: Response,

) -> dict:
    """

    :param response:
    :return: dict
    """

    response.delete_cookie("token")
    return dict(
        message="Logged out successfully"
    )