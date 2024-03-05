"""
Legislative data API route
"""

from fastapi import APIRouter

from legislative_data.utils import bills_supporters_and_opposers, legislator_bill_votes

router = APIRouter(prefix="/info", tags=["info"])


@router.get("/legislator-bill-votes")
def legislator_bill_votes_endpoint():
    data = legislator_bill_votes()

    return data


@router.get("/bills-supporters-and-opposers")
def bills_supporters_and_opposers_endpoint():
    data = bills_supporters_and_opposers()

    return data
