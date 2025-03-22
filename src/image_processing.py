import cv2 as cv
import numpy as np
import os
from src.constants import CUBE_FACE_POSITIONING, COLOR_MAP, COLOR_NUMBER_MAP

def extract_hsv_from_cubies(image) -> list:
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

def process_image_files(image_dir_path: str):
    full_cube_hsv = []
    full_paths = [os.path.join(image_dir_path, image) for image in os.listdir(image_dir_path)]
    sorted_dir_list = sorted(full_paths, key=os.path.getmtime)
    for path in sorted_dir_list:
        print(path)
    #Process each cube face in order captured
    for file in sorted_dir_list:
        if file.endswith(("jpg", "png")):
            file_path = os.path.join(image_dir_path, file)
            image = cv.imread(file_path)
                
            hsv_face = extract_hsv_from_cubies(image)

            full_cube_hsv.append(hsv_face)
            #positioning on cube face relative to center_cube_pos to determine center of each cubie
    
    return full_cube_hsv

def determine_color_of_cubie(hsv_value) -> str:
    for color, (lower, upper) in COLOR_MAP.items():
        lower = np.array(lower)
        upper = np.array(upper)
        if (lower <= hsv_value).all() and (upper >= hsv_value).all():
            if color == "red2":
                return "red"
            return color
        
    return "unknown"

def get_colors_from_hsv(cube_hsv):
    cube_colors = []
    for face in cube_hsv:
        color_f = []
        for row in range(len(face)):
            color_r = []
            for col in range(len(face[0])):
                cubie_c = determine_color_of_cubie(face[row][col])
                color_r.append(cubie_c)
            color_f.append(color_r)
        cube_colors.append(color_f)
    return cube_colors

def convert_image_colors_orientation(colors: list):
    # inverse = {0: 2, 1: 1, 2: 0}
    for face in colors:
        face[0][0], face[2][2] = face[2][2], face[0][0]
        face[0][1], face[2][1] = face[2][1], face[0][1]
        face[0][2], face[2][0] = face[2][0], face[0][2]
        face[1][0], face[1][2] = face[1][2], face[1][0]
    
    return colors

def cube_to_string(cube) -> str:
    cube_to_string = []
    for face in cube:
        face_string = cube_face_to_string(face)
        cube_to_string.extend(face_string)
    return cube_to_string

def cube_face_to_string(cube_face) -> str:
    for row in range(len(cube_face)):
        for col in range(len(cube_face[0])):
            cube_face[row][col] = COLOR_NUMBER_MAP[cube_face[row][col]]
    return list(map(str, sum(cube_face, [])))
