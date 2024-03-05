"""
API Exceptions
"""

from typing import Dict
from typing_extensions import Annotated, Doc
from fastapi.exceptions import HTTPException
from requests import codes


class MissingInfoException(HTTPException):
    """
    Exception raised when missing some info
    """

    def __init__(self) -> None:
        super().__init__(status_code=codes.BAD_REQUEST, detail="Missing info")


class VoteNotFound(HTTPException):
    """
    Exception raised when vote not found
    """

    def __init__(self) -> None:
        super().__init__(status_code=codes.NOT_FOUND, detail="Vote not found")
