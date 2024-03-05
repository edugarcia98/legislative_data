"""
API Exceptions
"""

from fastapi.exceptions import HTTPException
from requests import codes


class MissingInfoException(HTTPException):
    def __init__(self) -> None:
        super().__init__(status_code=codes.BAD_REQUEST, detail="Missing info")
