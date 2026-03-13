from datetime import datetime, timezone

from fastapi import APIRouter, Depends

from app.exceptions import NotFoundAPIException
from app.Public.dao import PublicDao
from app.Public.schemas import PublicSchema, PublicUpdateS
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("/create")
async def create_posts(public: PublicSchema, user: Users = Depends(get_current_user)):
    """

    create a new post

    :param public
    :return: None
    """

    await PublicDao.add(
        title=public.title,
        content=public.content,
        author_id=user.id,
        created_at=datetime.now(timezone.utc),
    )

@router.get("/get_posts{author_id}/")
async def get_posts_by_filter(author_id: str, title: str, content:str):

@router.get("/get_posts")
async def get_posts(limit: int, offset: int,suppression:bool):
    posts = await PublicDao.get_post(limit, offset,suppression)
    return posts




@router.get("/answer/{id}")
async def get_post(id: int, user=Depends(get_current_user)):
    post = await PublicDao.get_count_like_by_post_id(id, user.id)

    if not post:
        raise NotFoundAPIException()
    return dict(
        content={
            "author": {user.id, user.email},
            "likes_count": post,
        }
    )


@router.post("/like/{id}")
async def like_post(id: int, user: Users = Depends(get_current_user)):
    await PublicDao.set_like_by_post(id, user.id)


@router.patch("/update/{id}")
async def update_post(
    id: int, public: PublicUpdateS, user: Users = Depends(get_current_user)
):
    data_for_update = public.model_dump(exclude_unset=True, exclude_none=True)
    await PublicDao.update_posts(id, user.id, data_for_update)

    return True


@router.delete("/{id}")
async def delete_post(id: int, user: Users = Depends(get_current_user)):
    await PublicDao.delete_post(id, user.id)
