from sqlalchemy import select, and_, update, insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.Public.models import Publics, Likes
from app.dao.base import BaseDao


class PublicDao(BaseDao):
    model = Publics

    @classmethod
    async def delete_post(cls, id: int, user_id: int):
        async with AsyncSession() as session:
            posts = (
                update(Publics)
                .where(and_(Publics.id == id, Publics.owner_id == user_id))
                .values(deleted_at=True)

            )

            await session.execute(posts)
            await session.commit()


class LikeDao(BaseDao):
    model = Likes

    @classmethod
    async def add_like(cls, id: int, user_id: int):
        async with AsyncSession() as session:
            likes = (
                select(Likes.user_id)
                .where(
                    and_(Likes.user_id == user_id, Likes.public_id == id))
            )

            if likes:
                return None

            add_likes = (
                insert(Likes)
                .values(
                    public_id=id,
                    user_id=user_id
                )
                .returning(Likes.id)
            )

            new_likes = await session.execute(add_likes)
            await session.commit()
            return new_likes.scalar()
