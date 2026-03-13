from sqlalchemy import insert, select
from sqlalchemy.exc import SQLAlchemyError

from app.database import async_session_maker
from app.logger import log


class BaseDao:
    model = None

    @classmethod
    async def find_all(cls, **filter_by):
        try:
            async with async_session_maker() as session:
                query = select(cls.model.__table__.columns).filter_by(**filter_by)
                result = await session.execute(query)
                return result.mappings().all()
        except (SQLAlchemyError, Exception) as e:
            pass
            # await ExceptionFindData(e)

    @classmethod
    async def find_by_id(cls, id):
        try:
            async with async_session_maker() as session:
                query = select(cls.model).filter_by(id=id)
                result = await session.execute(query)
                return result.scalar_one_or_none()
        except (SQLAlchemyError, Exception) as e:
            pass
            # await ExceptionFindData(e)

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        try:
            async with async_session_maker() as session:
                query = select(cls.model).filter_by(**filter_by)
                result = await session.execute(query)
                return result.scalar_one_or_none()
        except (SQLAlchemyError, Exception) as e:
            pass
            # await ExceptionFindData(e)

    @classmethod
    async def add(cls, **data):

        try:

            async with async_session_maker() as session:
                query = insert(cls.model).values(**data)
                await session.execute(query)
                await session.commit()
        except (SQLAlchemyError, Exception) as e:
            print(e)
            if isinstance(e, SQLAlchemyError):
                msg = f"Database Exc: Cannot add {data}"
            elif isinstance(e, Exception):
                msg = f"Unknown Exc: Cannot add {data}"
            log.error(msg, exc_info=True)

    @classmethod
    async def update(cls, **data):
        try:
            async with async_session_maker() as session:
                query = insert(cls.model).values(**data)
                await session.execute(query)
                await session.commit()
        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg = f"Database Exc: Cannot update {cls.model}"
            elif isinstance(e, Exception):
                msg = f"Unknown Exc: Cannot update {cls.model}"
            log.error(msg, exc_info=True)
