from typing import List

from legislative_data.utils.constants import NOT_INFORMED
from legislative_data.utils.data import (
    bills_data,
    legislators_data,
    vote_results_data,
    votes_data,
)
from legislative_data.utils.exceptions import MissingInfoException, VoteNotFound


def legislator_bill_votes() -> List[dict]:
    """
    For every legislator available, checks:
    - How many bills did the legislator support (voted for the bill)
    - How many bills did the legislator oppose (voted against the bill)

    Returns:
        List[dict]: List containing information about supported and opposed bills
        by each legislator
    Raises:
        MissingInfoException: When legislator ID not found
    """
    result = []

    for legislator in legislators_data():
        if not (legislator_id := legislator.get("id")):
            raise MissingInfoException

        item = {
            "id": legislator_id,
            "legislator": legislator.get("name", "-"),
            "supported_bills": 0,
            "opposed_bills": 0,
        }

        for vote_result in vote_results_data():
            if vote_result.get("legislator_id") != legislator_id:
                continue

            key = (
                "supported_bills"
                if int(vote_result.get("vote_type")) == 1
                else "opposed_bills"
            )
            item[key] += 1
        
        result.append(item)
    
    return result


def _load_primary_sponsor(sponsor_id: str) -> str:
    """
    Loads primary sponsor name

    Args:
        sponsor_id (str): Sponsor ID
    Returns:
        str: Primary sponsor name
    """
    primary_sponsor = NOT_INFORMED

    for legislator in legislators_data():
        if legislator.get("id") == sponsor_id:
            primary_sponsor = legislator.get("name", NOT_INFORMED)
            break
    
    return primary_sponsor


def _load_vote_by_bill(bill_id: str) -> str:
    """
    Loads vote by bill ID

    Args:
        bill_id (str): Bill ID
    Returns:
        str: Vote ID
    Raises:
        VoteNotFound: When vote not found by bill ID
    """
    for vote in votes_data():
        if vote.get("bill_id") == bill_id:
            return vote.get("id")
    
    raise VoteNotFound



def bills_supporters_and_opposers() -> List[dict]:
    """
    For every bill available, checks:
    - How many legislators supported the bill
    - How many legislators opposed the bill
    - Who was the primary sponsor of the bill

    Returns:
        List[dict]: List containing information about legislators that supported and
        opposed the bills and its primary sponsors
    """
    result = []
    
    for bill in bills_data():
        if not (bill_id := bill.get("id")):
            raise MissingInfoException
        
        item = {
            "id": bill_id,
            "bill": bill.get("title", "-"),
            "supporters": 0,
            "opposers": 0,
            "primary_sponsor": _load_primary_sponsor(bill.get("sponsor_id", "-")),
        }

        vote_id = _load_vote_by_bill(bill_id)

        for vote_result in vote_results_data():
            if vote_result.get("vote_id") != vote_id:
                continue

            key = "supporters" if int(vote_result.get("vote_type")) == 1 else "opposers"
            item[key] += 1
        
        result.append(item)

    return result
