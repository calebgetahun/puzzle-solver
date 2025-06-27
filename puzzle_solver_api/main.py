from fastapi import FastAPI
from puzzle_solver_api.routers.uploads_router import router as uploads_router
from puzzle_solver_api.routers.cube_router import router as cube_router

app = FastAPI()

app.include_router(uploads_router, prefix="/uploads", tags=["uploads"])
app.include_router(cube_router, prefix="/cube", tags=["cube"])
