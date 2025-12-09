import json
import hashlib
import os
from typing import List

from fastapi import APIRouter, HTTPException, Request

from puzzle_solver_api.schemas import CubeState, SolutionResponse
from puzzle_solver_api.services.solver_service import InvalidCubeError, solve_from_faces

router = APIRouter(prefix="/v1/solutions", tags=["solutions"])

def _make_cache_key_from_faces(faces: List[List[str]]) -> str:
    """
    Creates a cache key string from the given cube faces
    """
    payload = json.dumps(faces, separators=(",", ":"))
    digest = hashlib.sha256(payload.encode()).hexdigest()
    return f"solver:v1:{digest}"

@router.post("", response_model=SolutionResponse)
async def create_solution(cube: CubeState, request: Request):
    """
    Tries to hit redis for cached solution before computing new one from core service.
    """
    faces = cube.faces
    cache_key = _make_cache_key_from_faces(faces)

    redis = getattr(request.app.state, "redis", None)

    # 1. Try Redis (L2 cache)
    if redis is not None:
        try:
            cached = await redis.get(cache_key)
            if cached is not None:
                print("[solutions] Redis cache HIT")
                return SolutionResponse(solution=cached)
            else:
                print("[solutions] Redis cache MISS")
        except Exception as e:
            # Fail-open: log and continue to compute solution
            print(f"[solutions] Redis error on GET: {e!r}")

    # 2. Cache miss (or Redis unavailable) → compute via service
    try:
        solution = solve_from_faces(faces)  # hits core LRU under the hood
    except InvalidCubeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to solve cube")

    # 3. Store result back to Redis (best-effort)
    if redis is not None:
        try:
            ttl_seconds = int(os.getenv("CACHE_TTL", "86400"))  # default 24h
            await redis.set(cache_key, solution, ex=ttl_seconds)
            print("[solutions] Redis cache SET")
        except Exception as e:
            print(f"[solutions] Redis error on SET: {e!r}")

    return SolutionResponse(solution=solution)
