import kociemba
from puzzle_solver_core.src.constants import COLOR_LETTER_MAP
from puzzle_solver_core.src.Cube import Cube
from functools import lru_cache

def color_to_face(face: list):
    face_s = []
    for cubie in face:
        face_s.append(COLOR_LETTER_MAP[cubie])
    return face_s

def create_cube_string(cube: Cube):
    cube_string = []
    
    for face in cube.cube_faces:
        cube_string.extend(color_to_face(face))

    return "".join(cube_string)

def solve_cube(cube: Cube):
    cube_string = create_cube_string(cube)
    return _solve_cube_string(cube_string)

@lru_cache(maxsize=2048)
def _solve_cube_string(cube_string: str) -> str:
    """
    Solve a canonical 54-char cube string with caching.
    """
    return kociemba.solve(cube_string)
