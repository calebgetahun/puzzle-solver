from typing import List, Optional
from fastapi import APIRouter, UploadFile, File, HTTPException, Query
from puzzle_solver_core.src.image_processing_core import image_bytes_to_colors, process_image_files
from ..schemas import ScanResponse, HSVResponse

router = APIRouter(prefix="v1/scans", tags=["scans"])

async def _read_cube_images(images: List[UploadFile]) -> List[bytes]:
    if len(images) != 6:
        raise ValueError("cube must have 6 images exactly")

    return [await image.read() for image in images]

@router.post("", response_model=ScanResponse)
async def create_scan(images: List[UploadFile] = File(...), include_hsv: bool = False):
    """
    Take 6 images and return a cube state (faces). Ordering of images is specific to agreed upon face color ordering    
    """
    try:
        cube_image_bytes = await _read_cube_images(images)
        cube_faces = image_bytes_to_colors(cube_image_bytes)

        response = ScanResponse(faces=cube_faces)

        if include_hsv:
            hsv_values = process_image_files(cube_image_bytes)
            response.hsv_debug = hsv_values
        
        return response
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Server error")
    
@router.post("/hsv", response_model=HSVResponse)
async def scan_hsv_values(images: List[UploadFile] = File(...)):
    """
    Debug endpoint: returns raw HSV values for cube images
    """
    try:
        cube_image_bytes = _read_cube_images(images)
        hsv_values = process_image_files(cube_image_bytes)
        return HSVResponse(hsv_values)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Server error")