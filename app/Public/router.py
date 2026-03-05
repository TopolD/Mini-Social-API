from datetime import datetime, timezone

from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from app.Public.dao import PublicDao
from app.Public.schemas import PublicUpdateS
from app.exceptions import NotFoundAPIException
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)


@router.get("/get_posts")
async def get_posts(limit:int,offset:int):
    posts = await PublicDao.get_post(limit,offset)
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


@router.get("/get_post/{id}")
async def get_post(id: int, user=Depends(get_current_user)):
    post = await PublicDao.find_post_by_id(id)
    count_like = await PublicDao.get_len_like(id)
    if not post:
        raise NotFoundAPIException()
    return JSONResponse(
        content={
            "author": {user.id, user.email},
            "likes_count": count_like,
        })


@router.patch("/update/{id}")
async def update_post(id: int, public: PublicUpdateS, user: Users = Depends(get_current_user)):
    data_for_update = public.model_dump(exclude_unset=True)
    update_res = await PublicDao.update_public(id, user, data_for_update)
    if not update_res:
        raise NotFoundAPIException()
    return True


@router.delete("/delete/{id}")
async def delete_post(id: int, user: Users = Depends(get_current_user)):
    target_posts = await PublicDao.delete_post(id, user.id)
    if not target_posts:
        raise NotFoundAPIException()
