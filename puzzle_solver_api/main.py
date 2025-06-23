from typing import Union, List
from fastapi import FastAPI, File, UploadFile, APIRouter
from pydantic import BaseModel
from puzzle_solver_core.src.Cube import Cube
from puzzle_solver_core.src.image_processing_core import image_bytes_to_colors

router = APIRouter()

@router.get("/solve_cube")
async def upload_images(images: List[UploadFile]):
    cube_image_bytes = [await image.read() for image in images]

    # Pass the list of bytes directly to your processing function
    cube_faces = image_bytes_to_colors(cube_image_bytes)
    cube = Cube(cube_faces)
    solution = cube.solution()
    return {"Solution": solution}

app = FastAPI()

class InputModel(BaseModel):
    scramble: str


# @app.post("/solve")
# def solve_scramble(scramble: InputModel):
#     solution = api_process_input(scramble.scramble)
#     return {"output": solution}

# @app.post("/upload_cube_faces")
# def upload_cube(images: List[UploadFile]):
#     return