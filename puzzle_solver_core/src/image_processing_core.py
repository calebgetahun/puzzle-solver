import cv2 as cv
import numpy as np
from typing import List
from puzzle_solver_core.src.constants import CUBE_FACE_POSITIONING, COLOR_MAP

def extract_hsv_from_cubies(image) -> list:
    """
    takes in singular image of cube face and outputs the colors as a list from top left to bottom right

    Args:
        image: a byte encoded image
    
    Returns:
        list[int] which represents the hsv value of each individual cubie in the cube face
    
    """
    #read image size (should be square based on previous calculations)
    image_size = image.shape[0]
    center_cubie_pos = int(image_size / 6)
    hsv_cubies_face = []
    
    #read cubies from left to right, top to bottom. Start from 1/6, 3/6, 5/6 to store color in the middle of each cubie
    for row in CUBE_FACE_POSITIONING:
        curr_row = []
        for col in CUBE_FACE_POSITIONING:
            #positioning on cube face relative to center_cube_pos to determine center of each cubie
            curr_pixel = image[center_cubie_pos * row, center_cubie_pos * col]
            curr_hsv = cv.cvtColor(np.uint8([[curr_pixel]]), cv.COLOR_BGR2HSV)
            curr_row.append(curr_hsv[0][0].tolist())

        hsv_cubies_face.append(curr_row)
    
    return hsv_cubies_face

def process_image_files(cube_image_bytes: List[bytes]):
    """
    This function takes as input the entire cube as byte encoded images and converts them into the hsv color space used by opencv
    This is then used to create an image based on the coloring and notation system used to solve the cube

    Args:
        list 

    """

    images = [cv.imdecode(np.frombuffer(i, np.uint8), cv.IMREAD_COLOR) for i in cube_image_bytes]
    full_cube_hsv = []
    
    for image in images:

        hsv_face = extract_hsv_from_cubies(image)

        full_cube_hsv.append(hsv_face)
        #positioning on cube face relative to center_cube_pos to determine center of each cubie
    
    return full_cube_hsv

def determine_color_of_cubie(hsv_value) -> str:
    for color, (lower, upper) in COLOR_MAP.items():
        lower = np.array(lower)
        upper = np.array(upper)
        if (lower <= hsv_value).all() and (upper >= hsv_value).all():
            if color == "R2":
                return "R"
            return color
        
    return "unknown"

def get_colors_from_hsv(cube_hsv):
    cube_colors = []
    for face in cube_hsv:
        color_f = []
        for row in range(len(face)):
            for col in range(len(face[0])):
                color_f.append(determine_color_of_cubie(face[row][col]))
        cube_colors.append(color_f)
    return cube_colors

def image_bytes_to_colors(image_bytes: List[bytes]) -> List[List[str]]:
    cube_hsv = process_image_files(image_bytes)
    colored_cube = get_colors_from_hsv(cube_hsv)
    return colored_cube
