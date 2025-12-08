from typing import List
from puzzle_solver_core.src.Cube import Cube
from puzzle_solver_core.src.kociemba_solver_core import solve_cube

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
