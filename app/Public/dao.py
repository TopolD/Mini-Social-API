from sqlalchemy import select, and_, update, insert, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.Public.models import Publics, likes
from app.dao.base import BaseDao


class PublicDao(BaseDao):
    model = Publics

    @classmethod
    async def delete_post(cls, id: int, user_id: int):
        async with AsyncSession() as session:
            query = (
                update(Publics)
                .where(and_(Publics.id == id, Publics.author_id == user_id))
                .values(deleted_at=True)

            )

            await session.execute(query)
            await session.commit()

    @classmethod
    async def update_posts(cls, id, user_id: int, data):
        async with AsyncSession() as session:
            query = (
                update(Publics)
                .where(and_(Publics.id == id, Publics.author_id == user_id))
                .values(**data)
            )
            await session.execute(query)
            await session.commit()

    @classmethod
    async def get_len_like(cls, public_id):
        async with AsyncSession() as session:
            query = select(func.count()).select_from(likes).where(likes.c.post_id == public_id)

            result = await session.execute(query)
            return result.scalar()

    @classmethod
    async def get_post(cls, limit: int, offset: int):
        async with AsyncSession() as session:
            query = select(Publics).limit(10).offset(0).order_by(Publics.id.desc())

            result = await session.execute(query)
            return result.scalars().all()
