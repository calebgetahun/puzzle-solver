import os

CUBE_FOLDER = os.path.join(os.path.dirname(__file__), "..", "assets", "cube_images")
FRAME_RATIO_CONSTANT = 0.3
CUBE_FACE_POSITIONING = (1, 3, 5)
CUBE_FACE_NOTATION = ["FRONT", "LEFT", "RIGHT", "BACK", "TOP", "BOTTOM"]
COLOR_MAP = {
    "red": [(0, 100, 75), (6, 255, 255)],
    "orange": [(7, 100, 75), (20, 255, 255)],
    "yellow": [(21, 100, 75), (35, 255, 255)],
    "green": [(36, 100, 75), (85, 255, 255)],
    "blue": [(100, 100, 75), (140, 255, 255)],
    "red2": [(160, 100, 75), (179 , 255, 255)],
    "white": [(0, 0, 150), (180, 60, 255)]
}

COLOR_NUMBER_MAP = {
    "white": 1,
    "green": 2,
    "blue": 3,
    "yellow": 4,
    "orange": 5,
    "red": 6
}