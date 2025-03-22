class Cube:
    def __init__(self, cube_faces):
        self.up = cube_faces[0]
        self.right = cube_faces[1]
        self.front = cube_faces[2]
        self.down = cube_faces[3]
        self.left =cube_faces[4]
        self.back = cube_faces[5]
        
        self.solution = []