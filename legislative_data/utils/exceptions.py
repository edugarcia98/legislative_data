"""
API Exceptions
"""

from typing import Dict
from typing_extensions import Annotated, Doc
from fastapi.exceptions import HTTPException
from requests import codes


class MissingInfoException(HTTPException):
    def __init__(self) -> None:
        super().__init__(status_code=codes.BAD_REQUEST, detail="Missing info")


class VoteNotFound(HTTPException):
    def __init__(self) -> None:
        super().__init__(status_code=codes.NOT_FOUND, detail="Vote not found")
