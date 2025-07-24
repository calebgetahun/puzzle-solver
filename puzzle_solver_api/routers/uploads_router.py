from typing import List
from fastapi import APIRouter, UploadFile, File, HTTPException
from puzzle_solver_core.src.image_processing_core import image_bytes_to_colors, process_image_files

router = APIRouter()

@router.post("/images")
async def upload_images(images: List[UploadFile] = File(...)):
    try:
        cube_image_bytes = [await image.read() for image in images]
        cube_faces = image_bytes_to_colors(cube_image_bytes)
        return {"cube_faces": cube_faces}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server error")

@router.post("/hsv_values")
async def hsv_cube_faces(images: List[UploadFile] = File(...)):
    try:
        cube_image_bytes = [await image.read() for image in images]
        hsv_values = process_image_files(cube_image_bytes)
        return {"hsv_cube": hsv_values}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server error")