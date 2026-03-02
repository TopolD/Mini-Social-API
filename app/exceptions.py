from fastapi import HTTPException, status


class BaseAPIException(HTTPException):
    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail: str = "API error"

    def __init__(self, detail: str | None = None):
        super().__init__(
            status_code=self.status_code,
            detail=detail or self.detail,
        )



class NotFoundAPIException(BaseAPIException):
    status_code: int = status.HTTP_404_NOT_FOUND
    detail: str = "Not Found"

class UserAlreadyExistsException(BaseAPIException):
    status_code: int = status.HTTP_409_CONFLICT
    detail: str = "User already exists"

class IncorrectEmailOrPasswordException(BaseAPIException):
    status_code: int = status.HTTP_400_BAD_REQUEST
    detail: str = "Incorrect email or password"

class TokenExpiredException(BaseAPIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен истек"


class TokenAbsentException(BaseAPIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен отсутствует"


class IncorrectTokenFormatException(BaseAPIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверный формат токена"


class UserIsNotPresentException(BaseAPIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Пользователь не найден"


