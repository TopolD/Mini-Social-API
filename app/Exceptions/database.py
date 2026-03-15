from sqlalchemy.exc import SQLAlchemyError

from app.logger import log


class ExceptionHandlerDatabase(SQLAlchemyError):
    message: str = "Database Exc"

    def __init__(self, message: str | None = None):
        super().__init__(message or self.message)
        log.error(message or self.message, exc_info=True)


class NotFindData(ExceptionHandlerDatabase):
    message: str = "Cannot  find data"


class NotAddData(ExceptionHandlerDatabase):
    message: str = "Cannot  add"


class NotUpdateData(ExceptionHandlerDatabase):
    message: str = "Cannot  update"
