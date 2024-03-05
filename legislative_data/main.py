"""
API main
"""

from fastapi import FastAPI

from legislative_data.routers.info import router as info_router

app = FastAPI()

app.include_router(info_router)


@app.get("/")
def home() -> dict:
    return {"success": True}
