from contextlib import asynccontextmanager
from typing import AsyncIterator
from redis.asyncio  import Redis
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


from app.config import settings
from app.routers import router

# @asynccontextmanager
# async def lifespan(_: FastAPI) -> AsyncIterator[None]:
#     redis = Redis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}")
#     FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
#     yield


app = FastAPI(
    title="For Interview",
    version="0.1.0",
    root_path="/api",
)




@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"detail": "invalid data"},
    )

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8080)
