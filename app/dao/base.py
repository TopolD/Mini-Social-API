from sqlalchemy import insert, select
from sqlalchemy.exc import SQLAlchemyError

from app.database import async_session_maker
from app.Exceptions.database import NotAddData, NotFindData, NotUpdateData
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

        except SQLAlchemyError as e:
            log.error(e, exc_info=True)
            raise NotFindData() from e

        except Exception as e:
            log.error(e, exc_info=True)
            raise

    @classmethod
    async def find_by_id(cls, id):
        try:
            async with async_session_maker() as session:
                query = select(cls.model).filter_by(id=id)
                result = await session.execute(query)
                return result.scalar_one_or_none()

        except SQLAlchemyError as e:
            log.error(e, exc_info=True)
            raise NotFindData() from e

        except Exception as e:
            log.error(e, exc_info=True)
            raise

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        try:
            async with async_session_maker() as session:
                query = select(cls.model).filter_by(**filter_by)
                result = await session.execute(query)
                return result.scalar_one_or_none()

        except SQLAlchemyError as e:
            log.error(e, exc_info=True)
            raise NotFindData() from e

        except Exception as e:
            log.error(e, exc_info=True)
            raise

    @classmethod
    async def add(cls, **data):

        try:

            async with async_session_maker() as session:
                query = insert(cls.model).values(**data)
                await session.execute(query)
                await session.commit()

        except SQLAlchemyError as e:
            log.error(e, exc_info=True)
            raise NotAddData() from e

        except Exception as e:
            log.error(e, exc_info=True)
            raise

    @classmethod
    async def update(cls, **data):
        try:
            async with async_session_maker() as session:
                query = insert(cls.model).values(**data)
                await session.execute(query)
                await session.commit()
        except SQLAlchemyError as e:
            log.error(e, exc_info=True)
            raise NotUpdateData() from e

        except Exception as e:
            log.error(e, exc_info=True)
            raise
