import os

CUBE_FOLDER = os.path.join(os.path.dirname(__file__), "..", "assets", "cube_images")
FRAME_RATIO_CONSTANT = 0.3
CUBE_FACE_POSITIONING = (1, 3, 5)
COLOR_MAP = {
    "red": [(0, 100, 100), (10, 255, 255)],
    "orange": [(11, 100, 100), (20, 255, 255)],
    "yellow": [(21, 100, 100), (35, 255, 255)],
    "green": [(36, 100, 100), (85, 255, 255)],
    "blue": [(100, 100, 100), (140, 255, 255)],
    "red2": [(160, 100, 100), (179 , 255, 255)],
    "white": [(0, 0, 200), (180, 30, 255)]
}