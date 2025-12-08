from typing import List
from fastapi import APIRouter, HTTPException

from puzzle_solver_api.schemas import CubeState, SolutionResponse
from puzzle_solver_api.services.solver_service import InvalidCubeError, solve_from_faces

router = APIRouter(prefix="/v1", tags=["solutions"])

@router.post("/solutions", response_model=SolutionResponse)
async def create_solution(cube: CubeState):
    try:
        solution = solve_from_faces(cube.faces)
        return SolutionResponse(solution=solution)
    except InvalidCubeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to solve cube")
