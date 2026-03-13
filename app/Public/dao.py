from sqlalchemy import and_, func, select, update
from sqlalchemy.dialects.postgresql import insert as pq_insert

from app.dao.base import BaseDao
from app.database import async_session_maker
from app.Public.models import Likes, Publics


class PublicDao(BaseDao):
    model = Publics

    @classmethod
    async def delete_post(cls, id: int, user_id: int):
        async with async_session_maker() as session:
            query = (
                update(Publics)
                .where(and_(Publics.id == id, Publics.author_id == user_id))
                .values(deleted_at=True)
            )

            await session.execute(query)
            await session.commit()

    @classmethod
    async def update_posts(cls, id: int, user_id: int, data):
        async with async_session_maker() as session:
            query = (
                update(Publics)
                .where(and_(Publics.id == id, Publics.author_id == user_id))
                .values(**data)
            )
            await session.execute(query)
            await session.commit()

    @classmethod
    async def get_post(cls, limit: int, offset: int, suppression: bool = False):
        async with async_session_maker() as session:
            query = (
                select(Publics)
                .where(Publics.deleted_at.is_(suppression))
                .limit(limit)
                .offset(offset)
                .order_by(Publics.id.desc())
            )

            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def get_count_like_by_post_id(cls, id: int, user_id: int):
        async with async_session_maker() as session:
            query = (
                select(func.count().label("like_count"))
                .select_from(Likes)
                .join(Publics, Likes.c.public_id == Publics.id)
                .where(and_(Publics.id == id, Publics.author_id == user_id))
                .group_by(Publics.id)
            )
            result = await session.execute(query)
            return result.scalar()

    @classmethod
    async def set_like_by_post(cls, post_id: int, user_id: int):
        async with async_session_maker() as session:
            query = pq_insert(Likes).values(
                public_id=post_id,
                user_id=user_id,
            )

            query = query.on_conflict_do_nothing(
                index_elements=["public_id", "user_id"]
            )
            await session.execute(query)
            await session.commit()
