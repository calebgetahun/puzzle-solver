from typing import List
from puzzle_solver_core.src.Cube import Cube
from puzzle_solver_core.src.kociemba_solver_core import solve_cube
from puzzle_solver_core.src.image_processing_core import image_bytes_to_colors, process_image_files

class InvalidCubeError(Exception):
    pass

def solve_from_faces(faces: List[List[str]]) -> str:
    """
    Application-level use case:
    - Takes raw faces (from HTTP / CLI / tests)
    - Builds the domain Cube
    - Calls the core logic
    - Normalizes domain errors
    """
    try:
        cube = Cube(faces)
    except ValueError as e:
        raise InvalidCubeError(str(e)) from e

    return solve_cube(cube)

def scan_faces_from_images(image_bytes: List[bytes]) -> List[List[str]]:
    """
    Application-level use case for image scanning:
    - Takes raw image bytes (6 images for cube faces)
    - Processes images to extract colors
    - Returns cube face data
    """
    if len(image_bytes) != 6:
        raise ValueError("cube must have 6 images exactly")
    
    return image_bytes_to_colors(image_bytes)

def get_hsv_debug_values(image_bytes: List[bytes]) -> List[List[List[List[int]]]]:
    """
    Debug use case:
    - Takes raw image bytes
    - Returns HSV values for analysis
    """
    if len(image_bytes) != 6:
        raise ValueError("cube must have 6 images exactly")
    
    return process_image_files(image_bytes)
