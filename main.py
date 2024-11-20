import cv2 as cv
import os
import numpy as np
from src.constants import FRAME_RATIO_CONSTANT, CUBE_FOLDER, CUBE_FACE_NOTATION
from src import image_processing

def main():
    #default camera capture
    capture = cv.VideoCapture(0)

    #number image captured
    image_count = 0

    while True:
        ret, frame = capture.read()
        if not ret:
            break

        frame_height, frame_width = frame.shape[:2]
        frame_ratio = frame_height/frame_width

        #Using the ratio of camera width to height, determine a square area of the screen to capture the cube details
        square_height = int(frame_height * FRAME_RATIO_CONSTANT)
        square_width = int(frame_width * frame_ratio * FRAME_RATIO_CONSTANT)

        #coordinates of the top left corner of our square capture box
        x = (frame_width - square_width) // 2
        y = (frame_height - square_height) // 2

        square_frame = frame[y:y+square_height, x:x+square_width]

        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(frame,
                f"ALIGN CUBE FACE. PRESS 's' TO CAPTURE. CURRENT FACE: {CUBE_FACE_NOTATION[image_count % 6]}",
                (50, 50),
                font,
                1,
                (0, 255, 255),
                2,
                cv.LINE_4,)
        
        #draw 3x3 cube lines into frame screen
        cv.rectangle(frame, (x, y), (x + square_width, y + square_height), (255, 0, 0), 2)
        cv.line(frame, (x + int(square_width / 3), y), (x + int(square_width / 3), y + square_height), (255, 0, 0), 2)
        cv.line(frame, (x + int(2 * square_width / 3), y), (x + int(2* square_width / 3), y + square_height), (255, 0, 0), 2)
        cv.line(frame, (x, y + int(square_height / 3)), (x + square_width, y + int(square_height / 3)), (255, 0, 0), 2)
        cv.line(frame, (x, y + int(2 * square_height / 3)), (x + square_width, y + int(2 * square_height / 3)), (255, 0, 0), 2)

        cv.imshow("Square shape frame", frame)

        #key directions to quit or save cube image file to cube images folder 
        key = cv.waitKey(1) & 0xFF
        if key == ord('s'):
            image_name = f"{CUBE_FACE_NOTATION[image_count % 6]}_FACE.jpg"
            os.makedirs(CUBE_FOLDER, exist_ok=True)
            cv.imwrite(os.path.join(CUBE_FOLDER, image_name), square_frame)
            print(f"image saved as {image_name}")
            image_count += 1
            if image_count == 6:
                break
            #TODO: show image for brief time period after screenshot

        if key == ord('q'):
            break

    capture.release()
    cv.destroyAllWindows()

    #hsv_values of cube
    cube = image_processing.process_image_files(CUBE_FOLDER)
    #colors of cube from hsv_values
    cube_colored = get_colors_from_hsv(cube)

    ## Printing functions ##
    #cube colors for each face
    # for i in range (len(cube_colored)):
    #     print(f"face {CUBE_FACE_NOTATION[i]}")
    #     for row in cube_colored[i]:
    #         print(row)
    
    # hsv value for each face
    # for row in range(len(cube)):
    #     for col in range(len(cube[0])):
    #         print(cube[row][col])

def get_colors_from_hsv(cube_hsv):
    cube_colors = []
    for face in cube_hsv:
        color_f = []
        for row in range(len(face)):
            color_r = []
            for col in range(len(face[0])):
                cubie_c = image_processing.determine_color_of_cubie(face[row][col])
                color_r.append(cubie_c)
            color_f.append(color_r)
        cube_colors.append(color_f)
    return cube_colors

if __name__ == "__main__":
    main()
