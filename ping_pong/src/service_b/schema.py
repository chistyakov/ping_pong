from typing import Optional, List

from pydantic import BaseModel


class DigitsOutput(BaseModel):
    digits: Optional[List[int]]
    avg: Optional[float]
    min: Optional[int]
    max: Optional[int]
