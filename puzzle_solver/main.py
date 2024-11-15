import cv2 as cv
import os
import numpy as np

FRAME_RATIO_CONSTANT = 0.33

#default camera capture
capture = cv.VideoCapture(0)

#number image captured
image_count = 1

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
               f'CAPTURE EACH SIDE OF THE CUBE. CURRENT PICTURE: {image_count}',
               (50, 50),
               font,
               1,
               (0, 255, 255),
               2,
               cv.LINE_4,)
    
    cv.rectangle(frame, (x, y), (x + square_width, y + square_height), (255, 0, 0), 2)
    cv.imshow("Square shape frame", frame)

    key = cv.waitKey(1) & 0xFF
    if key == ord('s'):
        image_name = f"captured_image_{image_count}.jpg"

        cube_folder = os.path.join(os.path.dirname(__file__), "assets/cube_images")
        os.makedirs(cube_folder, exist_ok=True)

        cv.imwrite(os.path.join(cube_folder, image_name), square_frame)
        print(f"image saved as {image_name}")
        image_count += 1

    if key == ord('q'):
        break

capture.release()
cv.destroyAllWindows()

