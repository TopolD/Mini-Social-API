from datetime import datetime, timezone

from fastapi import APIRouter, Depends

from app.Public.dao import PublicDao, LikeDao
from app.exceptions import NotFoundAPIException
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)


@router.get("/get_posts")
async def get_posts(user: Users = Depends(get_current_user)):
    posts = await PublicDao.find_all(owner_id=user.id)
    return posts


@router.post("/create")
async def create_posts(title: str, content: str, user: Users = Depends(get_current_user)):
    """

    create a new post

    :param title:
    :param content:
    :param user:
    :return: new_posts
    """
    new_posts = await PublicDao.add(
        title=title,
        content=content,
        owner_id=user.id,
        created_at=datetime.now(timezone.utc)
    )

    return new_posts


@router.delete("/{id}")
async def delete_post(id: int, user: Users = Depends(get_current_user)):
    target_posts = await PublicDao.delete_post(id, user.id)
    if not target_posts:
        raise NotFoundAPIException()


@router.post("/{id}")
async def set_like(id: int, user: Users = Depends(get_current_user)):
    """
    set like for post

    :param id:
    :param user:
    :return: new_like
    """
    new_like = await LikeDao.add_like(id, user.id)
    if not new_like:
        raise NotFoundAPIException()
    return new_like
