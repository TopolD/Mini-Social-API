import asyncio

import pytest
import json


from sqlalchemy import insert


from app.config import settings
from app.database import Base,async_session_maker,engine

from app.main import app as fastapi_app
from app.users.models import Users


from httpx import AsyncClient,ASGITransport


@pytest.fixture(scope="session",autouse=True)
async def repare_database():
    assert settings.MODE == 'TEST'

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


    def open_mock_json(model:str):
        with open (f"app/tests/mock_{model}.json",encoding="utf-8") as f:
            return json.load(f)

    users = open_mock_json('users')



    async with async_session_maker() as session:
        for Model, values in [
            (Users, users),
        ]:
            query = insert(Model).values(values)
            await session.execute(query)

        await session.commit()


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="function")
async def ac() :
    async with AsyncClient(transport=ASGITransport(app=fastapi_app),base_url="http://test") as ac:
        yield ac

@pytest.fixture(scope="session")
async def authenticated_ac() :
    async with AsyncClient(transport=ASGITransport(app=fastapi_app),base_url="http://test") as ac:
        response = await ac.post("/auth/login", json={
            "email":"test@test.com",
            "password":"test",
        })
        token = response.cookies.get("token")
        assert token
        ac.cookies.set("token",token)
        yield ac

@pytest.fixture(scope="function")
async def session():
    async with async_session_maker() as session:
        yield session