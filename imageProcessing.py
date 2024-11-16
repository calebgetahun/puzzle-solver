import cv2 as cv
import numpy as np
import os
import constants

def extract_hsv_from_cubies():
    #Process each cube face in order captured. Current number of faces: 1
    for file in os.listdir(constants.CUBE_FOLDER):
        if file.endswith(("jpg", "png")):
            file_path = os.path.join(constants.CUBE_FOLDER, file)
            image = cv.imread(file_path)

            #read image size (should be square based on previous calculations)
            image_size = image.shape[0]
            
            #read cubies from left to right, top to bottom. Start from 1/6, 3/6, 5/6 to read color (BGR) in the middle of each cubie
            center_cubie_pos = int(image_size / 6)
            hsv_cubies = []

            #positioning on cube face relative to center_cube_pos to determine center of each cubie
            face_pos = (1, 3, 5)

            for row in face_pos:
                curr_row = []
                for col in face_pos:
                    curr_pixel = image[center_cubie_pos * row, center_cubie_pos * col]
                    curr_hsv = cv.cvtColor(np.uint8([[curr_pixel]]), cv.COLOR_BGR2HSV)
                    curr_row.append(curr_hsv[0][0].tolist())

                hsv_cubies.append(curr_row)
            
            for cubie_row in hsv_cubies:
                print(cubie_row)