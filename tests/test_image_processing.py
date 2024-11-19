import pytest
import os
import sys
import cv2 as cv
from src.image_processing import extract_hsv_from_cubies, determine_color_of_cubie

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

#constants for file testing
test_image = os.path.join(os.path.dirname(__file__), "test_cube_face.png")
image = cv.imread(test_image)

# Test color reading for extracting hsv cubies for white, red, and orange faces. Currently using a digital asset for testing
def test_extract_hsv_from_cubies():
    assert extract_hsv_from_cubies(image)[0][2] == [0, 0, 255]
    assert extract_hsv_from_cubies(image)[1][1] == [0, 255, 255]
    assert extract_hsv_from_cubies(image)[2][0] == [19, 255, 255]
