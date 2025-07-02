import cv2 as cv
import numpy as np
from typing import List
from puzzle_solver_core.src.constants import CUBE_FACE_POSITIONING, COLOR_MAP

def extract_hsv_from_cubies(image: np.ndarray) -> list:
    """
    takes in singular image of cube face and outputs the colors as a list from top left to bottom right

    Args:
        image: a byte encoded image
    
    Returns:
        list[int] which represents the hsv value of each individual cubie in the cube face
    
    """

    if image is None or len(image.shape) != 3:
        raise ValueError("invalid image input.")
    #read image size (should be square based on previous calculations)
    h, w, _ = image.shape

    if h != w:
        raise ValueError(f"image must be a square. Got {h} x {w}")

    center_cubie_pos = int(h / 6)
    hsv_cubies_face = []
    
    #read cubies from left to right, top to bottom. Start from 1/6, 3/6, 5/6 to store color in the middle of each cubie
    for row in CUBE_FACE_POSITIONING:
        curr_row = []
        for col in CUBE_FACE_POSITIONING:
            y = center_cubie_pos * row
            x = center_cubie_pos * col

            if y >= h or x >= h:
                raise ValueError(f"image points out of bounds: ({y}, {x})")
        
            #positioning on cube face relative to center_cube_pos to determine center of each cubie
            curr_pixel = image[y, x]
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

    images = []
    for i, byte_data in enumerate(cube_image_bytes):
        np_arr = np.frombuffer(byte_data, np.uint8)
        image = cv.imdecode(np_arr, cv.IMREAD_COLOR)
        if image is None:
            raise ValueError(f"Image {i} could not be decoded.")
        images.append(image)

    full_cube_hsv = []
    for i, image in enumerate(images):
        try:
            hsv_face = extract_hsv_from_cubies(image)
            full_cube_hsv.append(hsv_face)
        except Exception as e:
            raise ValueError(f"Error processing cube face {i}: {str(e)}")

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
    for i, face in enumerate(cube_hsv):
        color_f = []
        for row in range(len(face)):
            for col in range(len(face[0])):
                curr_color = determine_color_of_cubie(face[row][col])
                if curr_color == "unknown":
                    raise ValueError(f"unknown color detected on face {i} at position ({row}, {col})")
                color_f.append(curr_color)
        cube_colors.append(color_f)
    return cube_colors

def image_bytes_to_colors(image_bytes: List[bytes]) -> List[List[str]]:
    cube_hsv = process_image_files(image_bytes)
    colored_cube = get_colors_from_hsv(cube_hsv)
    return colored_cube
