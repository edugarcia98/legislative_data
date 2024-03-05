from typing import List

from legislative_data.utils.data import (
    bills_data,
    legislators_data,
    vote_results_data,
    votes_data,
)
from legislative_data.utils.exceptions import MissingInfoException


def legislator_bill_votes() -> List[dict]:
    """
    For every legislator available, checks:
    - How many bills did the legislator support (voted for the bill)
    - How many bills did the legislator oppose (voted against the bill)

    Returns:
        List[dict]: List containing information about supported and opposed bills
        by each legislator
    """
    result = []
    legislators = legislators_data()

    for legislator in legislators:
        if not (legislator_id := legislator.get("id")):
            raise MissingInfoException

        item = {
            "id": legislator_id,
            "legislator": legislator.get("name", "-"),
            "supported_bills": 0,
            "opposed_bills": 0,
        }

        vote_results = vote_results_data()

        for vote_result in vote_results:
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


def bills_supporters_and_opposers() -> List[dict]:
    pass
