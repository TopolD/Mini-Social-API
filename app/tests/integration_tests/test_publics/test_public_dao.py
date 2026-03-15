import pytest

from app.Public.dao import PublicDao


@pytest.mark.parametrize("id,user_id", [(1, 1)])
async def test_delete_public_with_db(id: int, user_id: int):
    await PublicDao.delete_post(id, user_id)


@pytest.mark.parametrize(
    "id,user_id,data",
    [
        (1, 1, {"content": "animal", "title": "duck"}),
        (2, 1, {"content": "articles", "title": "example"}),
    ],
)
async def test_delete_public_with_db(id: int, user_id: int, data: dict):
    await PublicDao.update_posts(id, user_id, data)


async def test_get_public_with_db():
    posts = await PublicDao.get_post(10, 0)

    assert posts is not None


@pytest.mark.parametrize("id,user_id", [(1, 1)])
async def test_get_public_with_db_by_id(id: int, user_id: int):
    posts = await PublicDao.get_count_like_by_post_id(id, user_id)
    assert posts is not None


@pytest.mark.parametrize("id,user_id", [(1, 1)])
async def test_set_like_by_post(id: int, user_id: int):
    await PublicDao.set_like_by_post(id, user_id)


@pytest.mark.parametrize(
    "author_id,sort,order,title,content",
    [
        (1, "created_at", "desc", "dogs", "are"),
        (2, "like_count", "asc", "coffee", "in the morning"),
    ],
)
async def test_get_posts_by_filter(author_id, sort, order, title, content):
    await PublicDao.get_post_by_filters(author_id, sort, order, title, content)
