import pytest
import os
import sys
import cv2 as cv
from archive.image_processing import extract_hsv_from_cubies, determine_color_of_cubie, process_image_files

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

#constants for file testing
test_image = os.path.join(os.path.dirname(__file__), "test_cube_face.png")
test_image_dir_path = os.path.join(os.path.dirname(__file__), "test_assets")
image = cv.imread(test_image)

# Test color reading for extracting hsv cubies
def test_extract_hsv_from_cubies():
    assert extract_hsv_from_cubies(image)[0][2] == [0, 0, 255]
    assert extract_hsv_from_cubies(image)[1][1] == [0, 255, 255]
    assert extract_hsv_from_cubies(image)[2][0] == [19, 255, 255]


def test_determine_color_of_cubie():
    assert determine_color_of_cubie([15, 225, 255]) == "orange"
    assert determine_color_of_cubie([4, 200, 255]) == "red"
    assert determine_color_of_cubie([60, 225, 255]) == "green"
    assert determine_color_of_cubie([30, 225, 255]) == "yellow"

def test_accurate_color_depiction():
    #face that contains all colors
    hsv_face = process_image_files(test_image_dir_path)[3]
    assert determine_color_of_cubie(hsv_face[0][0]) == "yellow"
    assert determine_color_of_cubie(hsv_face[0][1]) == "blue"
    assert determine_color_of_cubie(hsv_face[0][2]) == "orange"
    assert determine_color_of_cubie(hsv_face[1][0]) == "orange"
    assert determine_color_of_cubie(hsv_face[1][1]) == "red"
    assert determine_color_of_cubie(hsv_face[1][2]) == "blue"
    assert determine_color_of_cubie(hsv_face[2][0]) == "yellow"
    assert determine_color_of_cubie(hsv_face[2][1]) == "green"
    assert determine_color_of_cubie(hsv_face[2][2]) == "white"