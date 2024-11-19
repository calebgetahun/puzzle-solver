import cv2 as cv
import numpy as np
import os
from src.constants import CUBE_FACE_POSITIONING, CUBE_FOLDER

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

def process_image_files():
    full_cube_hsv = []
    # sorted_dir_list = sorted()
      #Process each cube face in order captured
    for file in os.listdir(CUBE_FOLDER):
        if file.endswith(("jpg", "png")):
            file_path = os.path.join(CUBE_FOLDER, file)
            image = cv.imread(file_path)
                
            hsv_face = extract_hsv_from_cubies(image)

            full_cube_hsv.append(hsv_face)
            #positioning on cube face relative to center_cube_pos to determine center of each cubie
    
    for face in full_cube_hsv:
        print(face)
    
    return full_cube_hsv