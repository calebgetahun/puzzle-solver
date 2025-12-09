from typing import List
from puzzle_solver_core.src.Cube import Cube
from puzzle_solver_core.src.kociemba_solver_core import solve_cube
from puzzle_solver_core.src.image_processing_core import image_bytes_to_colors, process_image_files

class InvalidCubeError(Exception):
    pass

def solve_from_faces(faces: List[List[str]]) -> str:
    """
    Returns a solution string for the given cube faces.
    """
    try:
        cube = Cube(faces)
    except ValueError as e:
        raise InvalidCubeError(str(e)) from e

    return solve_cube(cube)

def scan_faces_from_images(image_bytes: List[bytes]) -> List[List[str]]:
    """
    Returns cube face colors from raw image bytes.
    """
    if len(image_bytes) != 6:
        raise ValueError("cube must have 6 images exactly")
    
    return image_bytes_to_colors(image_bytes)

def get_hsv_debug_values(image_bytes: List[bytes]) -> List[List[List[List[int]]]]:
    """
    Returns HSV values from raw image bytes (for debugging).
    """
    if len(image_bytes) != 6:
        raise ValueError("cube must have 6 images exactly")
    
    return process_image_files(image_bytes)
