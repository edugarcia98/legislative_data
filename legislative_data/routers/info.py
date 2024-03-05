from fastapi import APIRouter

from legislative_data.utils import legislator_bill_votes

router = APIRouter(prefix="/info", tags=["info"])


@router.get("/legislator-bill-votes")
def legislator_bill_votes_endpoint():
    data = legislator_bill_votes()

    return data