# schemas.py
from typing import List, Optional
from pydantic import BaseModel

class CubeState(BaseModel):
    # 6 faces x 9 stickers
    faces: List[List[str]]

class ScanResponse(BaseModel):
    faces: List[List[str]]
    hsv_debug: Optional[List[List[List[List[int]]]]] = None

class HSVResponse(BaseModel):
    hsv_cube: List[List[List[List[int]]]]

class SolutionResponse(BaseModel):
    solution: str