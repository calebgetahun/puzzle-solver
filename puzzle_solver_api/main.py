from contextlib import asynccontextmanager
import os

from fastapi import FastAPI
from redis import asyncio as aioredis  # redis-py 7.x import

from puzzle_solver_api.routers.scans_router import router as scans_router
from puzzle_solver_api.routers.solutions_router import router as solutions_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Default to local Redis if REDIS_URL not set
    redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")

    try:
        app.state.redis = aioredis.from_url(redis_url, decode_responses=True)
        print(f"[lifespan] Connected to Redis at {redis_url}")
    except Exception as e:
        app.state.redis = None
        print(f"[lifespan] Redis unavailable: {e}")

    yield

    if getattr(app.state, "redis", None):
        await app.state.redis.close()
        print("[lifespan] Redis connection closed")


app = FastAPI(lifespan=lifespan)

app.include_router(scans_router)
app.include_router(solutions_router)