import cv2 as cv
from puzzle_solver_core.src.Cube import Cube
from puzzle_solver_core.src.image_processing_core import image_bytes_to_colors
from puzzle_solver_core.src.kociemba_solver_core import solve_cube

FRAME_RATIO_CONSTANT = 0.3
CUBE_FACE_NOTATION = ["Orange", "Blue", "White", "Red", "Green", "Yellow"]
images = []

def capture():
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
            success, encoded_image = cv.imencode('.jpg', square_frame)
            if not success:
                raise ValueError("Image encoding failed")
            image_bytes = encoded_image.tobytes()
            images.append(image_bytes)

            image_count += 1
            if image_count == 6:
                break

        if key == ord('q'):
            break

    capture.release()
    cv.destroyAllWindows()

def output_solution(image_byte_list):
    if len(image_byte_list) != 6:
        raise ValueError(f"6 images needed to solve cube. Received {len(image_byte_list)} instead")
    colored_cube = image_bytes_to_colors(image_byte_list)
    cube = Cube(colored_cube)
    solution = solve_cube(cube)
    print(f"Here is your solution: {solution}")

if __name__ == "__main__":
    capture()
    output_solution(images)
