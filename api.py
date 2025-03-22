from typing import Union
from fastapi import FastAPI
from src.kociemba_solver import api_process_input
from pydantic import BaseModel

app = FastAPI()

class InputModel(BaseModel):
    scramble: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/solve")
def solve_scramble(scramble: InputModel):
    solution = api_process_input(scramble.scramble)
    return {"output": solution}