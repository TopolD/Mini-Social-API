from sqlalchemy import select, and_, update, insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.Public.models import Publics
from app.dao.base import BaseDao


class PublicDao(BaseDao):
    model = Publics

    @classmethod
    async def delete_post(cls, id: int, user_id: int):
        async with AsyncSession() as session:
            posts = (
                update(Publics)
                .where(and_(Publics.id == id, Publics.author_id == user_id))
                .values(deleted_at=True)

            )

            await session.execute(posts)
            await session.commit()


    @classmethod
    async def update_posts(cls, id,user_id: int,data):
        async with AsyncSession() as session:
            posts = (
                update(Publics)
                .where(and_(Publics.id == id, Publics.author_id == user_id))
                .values(**data)
            )
            await session.execute(posts)
            await session.commit()




