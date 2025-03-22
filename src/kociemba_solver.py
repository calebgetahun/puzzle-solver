import kociemba
from src.constants import COLOR_LETTER_MAP

class Cube_v0:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.solution = []

def main():

    """
             |************|
             |*U1**U2**U3*|
             |************|
             |*U4**U5**U6*|
             |************|
             |*U7**U8**U9*|
             |************|
 ************|************|************|************
 *L1**L2**L3*|*F1**F2**F3*|*R1**R2**R3*|*B1**B2**B3*
 ************|************|************|************
 *L4**L5**L6*|*F4**F5**F6*|*R4**R5**R6*|*B4**B5**B6*
 ************|************|************|************
 *L7**L8**L9*|*F7**F8**F9*|*R7**R8**R9*|*B7**B8**B9*
 ************|************|************|************
             |************|
             |*D1**D2**D3*|
             |************|
             |*D4**D5**D6*|
             |************|
             |*D7**D8**D9*|
             |************|
    
    scramble form: "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
    example scramble: B2 R' L2 D2 L2 B2 L' R2 D L' R' F2 U2 F D U2 L D2 R2 F2 D U' L' D' L2
    orientation is: F: white, L: green, R: blue, U: orange, D: red, B: yellow
    example scramble string = "FFLBUBDFLURDLRDRRRBLFLFDBRBUDUUDUBBURDLRLURBLFUDFBFFLD"
    
    """
    UP = ["W", "W", "G", "Y", "O", "Y", "R", "W", "G"]
    RIGHT = ["O", "B", "R", "G", "B", "R", "B", "B", "B"]
    FRONT = ["Y", "G", "W", "G", "W", "R", "Y", "B", "Y"]
    DOWN = ["O", "R", "O", "O", "R", "O", "Y", "Y", "O"]
    LEFT = ["B", "R", "G", "B", "G", "O", "B", "Y", "G"]
    BACK = ["W", "O", "R", "W", "Y", "W", "W", "G", "R"]


    scramble_string = []
    scramble_string.extend(color_to_face(UP))
    scramble_string.extend(color_to_face(RIGHT))
    scramble_string.extend(color_to_face(FRONT))
    scramble_string.extend(color_to_face(DOWN))
    scramble_string.extend(color_to_face(LEFT))
    scramble_string.extend(color_to_face(BACK))

    scramble = "".join(scramble_string)
    print(scramble)

    cube = Cube_v0(scramble)
    cube.solution = kociemba.solve(cube.initial_state)
    print(cube.solution)

def color_to_face(face: list):
    face_s = []
    for cubie in face:
        face_s.append(COLOR_LETTER_MAP[cubie])
    return face_s

def api_process_input(scramble: str):
    solution = kociemba.solve(scramble)
    return f"Here is your solution: {solution}"

if __name__ == "__main__":
    main()