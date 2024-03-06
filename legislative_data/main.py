"""
API main
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from legislative_data.routers.info import router as info_router

app = FastAPI()

app.include_router(info_router)

templates = Jinja2Templates(directory="legislative_data/templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request) -> HTMLResponse:
    """
    Home endpoint

    Args:
        request (Request): Request object
    Returns:
        HTMLResponse: Response in HTML
    """
    return templates.TemplateResponse("index.html", {"request": request})
