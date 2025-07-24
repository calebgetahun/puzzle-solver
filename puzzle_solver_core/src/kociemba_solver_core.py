import kociemba
from puzzle_solver_core.src.constants import COLOR_LETTER_MAP
from puzzle_solver_core.src.Cube import Cube

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
    return kociemba.solve(cube_string)