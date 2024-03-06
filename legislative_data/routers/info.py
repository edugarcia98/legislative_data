"""
Legislative data API route
"""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from legislative_data.utils import bills_supporters_and_opposers, legislator_bill_votes

router = APIRouter(prefix="/info", tags=["info"])

templates = Jinja2Templates(directory="legislative_data/templates")


@router.get("/legislator-bill-votes", response_class=HTMLResponse)
def legislator_bill_votes_endpoint(request: Request) -> HTMLResponse:
    """
    Endpoint that returns list containing info about supported and opposed bills
    by each legislator

    Args:
        request (Request): Request object
    Returns:
        HTMLResponse: Response in HTML
    """
    data = legislator_bill_votes()

    return templates.TemplateResponse(
        "legislator_bill_votes.html",
        {"request": request, "data": data},
    )


@router.get("/bills-supporters-and-opposers", response_class=HTMLResponse)
def bills_supporters_and_opposers_endpoint(request: Request) -> HTMLResponse:
    """
    Endpoint that returns list containing info about legislators that supported and
    opposed the bills and its primary sponsors

    Args:
        request (Request): Request object
    Returns:
        HTMLResponse: Response in HTML
    """
    data = bills_supporters_and_opposers()

    return templates.TemplateResponse(
        "bills_supporters_and_opposers.html",
        {"request": request, "data": data},
    )
