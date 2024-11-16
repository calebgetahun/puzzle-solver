import cv2 as cv
import numpy as np
import os
import constants

#Image processing
for file in os.listdir(constants.CUBE_FOLDER):
    if file.endswith(("jpg", "png")):
        file_path = os.path.join(constants.CUBE_FOLDER, file)
        image = cv.imread(file_path)

        #read image size (should be square based on previous calculations)
        image_size = image.shape[0]
        
        #read cubies from left to right, top to bottom. Start from 1/6, 3/6, 5/6 to read color (BGR) in the middle of each cubie
        center_cubie_pos = int(image_size / 6)
        cubies = []

        #top row of cubies
        color_one = image[center_cubie_pos, center_cubie_pos]
        color_two = image[center_cubie_pos, center_cubie_pos * 3]
        color_three = image[center_cubie_pos, center_cubie_pos * 5]

        cubies.append(color_one)
        cubies.append(color_two)
        cubies.append(color_three)

        #middle row of cubies
        color_four = image[center_cubie_pos * 3, center_cubie_pos]
        color_five = image[center_cubie_pos * 3, center_cubie_pos * 3]
        color_six = image[center_cubie_pos * 3, center_cubie_pos * 5]

        cubies.append(color_four)
        cubies.append(color_five)
        cubies.append(color_six)

        #bottome row of cubies
        color_seven = image[center_cubie_pos * 5, center_cubie_pos]
        color_eight = image[center_cubie_pos * 5, center_cubie_pos * 3]
        color_nine = image[center_cubie_pos * 5, center_cubie_pos * 5]

        cubies.append(color_seven)
        cubies.append(color_eight)
        cubies.append(color_nine)

        for cubie in cubies:
            print(cubie)