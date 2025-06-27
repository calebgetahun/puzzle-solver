from typing import List
from fastapi import APIRouter
from pydantic import BaseModel
from puzzle_solver_core.src.Cube import Cube
from puzzle_solver_core.src.kociemba_solver_core import solve_cube

class CubeModel(BaseModel):
    cube_faces: List[List[str]]

router = APIRouter()

@router.post("/solve")
async def upload_images(cube: List[List[str]]):
    solution = solve_cube(Cube(cube))
    return {"solution": solution}
