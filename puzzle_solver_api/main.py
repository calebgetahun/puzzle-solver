from fastapi import FastAPI
from puzzle_solver_api.routers.scans_router import router as scans_router
from puzzle_solver_api.routers.solutions_router import router as cube_router

app = FastAPI()

app.include_router(scans_router, prefix="/scans", tags=["uploads"])
app.include_router(cube_router, prefix="/cube", tags=["cube"])
