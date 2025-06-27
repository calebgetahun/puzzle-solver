from typing import List
from fastapi import APIRouter, UploadFile, File
from puzzle_solver_core.src.image_processing_core import image_bytes_to_colors

router = APIRouter()

@router.post("/images")
async def upload_images(images: List[UploadFile] = File(...)):
    cube_image_bytes = [await image.read() for image in images]
    cube_faces = image_bytes_to_colors(cube_image_bytes)
    return {"cube": cube_faces}