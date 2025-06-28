import logging
from typing import List
from fastapi import APIRouter, UploadFile, File, HTTPException
from puzzle_solver_core.src.image_processing_core import image_bytes_to_colors

router = APIRouter()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s',
)

logger = logging.getLogger(__name__)

@router.post("/images")
async def upload_images(images: List[UploadFile] = File(...)):
    logger.info(f"Received {len(images)} images")
    for image in images:
        logger.info(f"Image: {image.filename} - content_type: {image.content_type}")
    try:
        cube_image_bytes = [await image.read() for image in images]
        logger.info(f"Image byte sizes: {[len(b) for b in cube_image_bytes]}")
        cube_faces = image_bytes_to_colors(cube_image_bytes)
        return {"cube": cube_faces}
    except Exception as e:
        logger.exception("Error while processing images")
        raise HTTPException(status_code=500, detail=str(e))