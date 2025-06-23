from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CUBE_FOLDER = BASE_DIR / "assets" / "cube_images"
FRAME_RATIO_CONSTANT = 0.3
CUBE_FACE_POSITIONING = (1, 3, 5)
CUBE_FACE_NOTATION = ["UP", "RIGHT", "FRONT", "DOWN", "LEFT", "BACK"]
CUBE_FACE_COLORS = []

# COLOR_MAP = {
#     "red": [(0, 100, 75), (6, 255, 255)],
#     "orange": [(7, 100, 75), (20, 255, 255)],
#     "yellow": [(21, 100, 75), (35, 255, 255)],
#     "green": [(36, 100, 75), (85, 255, 255)],
#     "blue": [(100, 100, 75), (140, 255, 255)],
#     "red2": [(160, 100, 75), (179 , 255, 255)],
#     "white": [(0, 0, 150), (180, 60, 255)]
# }

COLOR_MAP = {
    "R": [(0, 100, 75), (6, 255, 255)],
    "O": [(7, 100, 75), (20, 255, 255)],
    "Y": [(21, 100, 75), (35, 255, 255)],
    "G": [(36, 100, 75), (85, 255, 255)],
    "B": [(100, 100, 75), (140, 255, 255)],
    "R2": [(160, 100, 75), (179 , 255, 255)],
    "W": [(0, 0, 150), (180, 60, 255)]
}

COLOR_NUMBER_MAP = {
    "white": 1,
    "green": 2,
    "blue": 3,
    "yellow": 4,
    "orange": 5,
    "red": 6
}

COLOR_LETTER_MAP = {
    "O": "U",
    "R": "D",
    "G": "L",
    "B": "R",
    "W": "F",
    "Y": "B"
}