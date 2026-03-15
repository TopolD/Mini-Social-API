import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "title,content",
    [
        ("cats", "cats are cute"),
    ],
)
async def test_create_public(title, content, authenticated_ac: AsyncClient):
    response = await authenticated_ac.post(
        "/posts/create", json={"title": title, "content": content}
    )

    assert response.status_code == 200


@pytest.mark.parametrize("id", ["1"])
async def test_create_like(id, authenticated_ac: AsyncClient):
    response = await authenticated_ac.post(f"/posts/like/{id}", json={"id": id})

    assert response.status_code == 200


@pytest.mark.parametrize("id", ["1"])
async def test_get_like_by_post(id, authenticated_ac: AsyncClient):
    response = await authenticated_ac.get(f"/posts/answer/{id}")

    assert response.status_code == 200


@pytest.mark.parametrize(
    "id,title,content,status_code",
    [
        ("1", "animal", None, 200),
        ("2", "article for people ", "people is beautiful", 200),
    ],
)
async def test_update_post(
    id, title, content, status_code, authenticated_ac: AsyncClient
):
    response = await authenticated_ac.patch(
        f"/posts/update/{id}", json={"id": id, "title": title, "content": content}
    )

    assert response.status_code == status_code


@pytest.mark.parametrize("id", ["1"])
async def test_delete_post(id, authenticated_ac: AsyncClient):
    response = await authenticated_ac.delete(f"/posts/{id}")

    assert response.status_code == 200
