from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel

from common.schema import DigitsIn

app = FastAPI()


class DigitsOut(BaseModel):
    digits: Optional[List[int]]
    min: Optional[int]
    max: Optional[int]
    avg: Optional[float]


@app.post("/pong")
def post_ping(digits_input: DigitsIn) -> DigitsOut:
    digits = digits_input.digits or []
    if not digits:
        return DigitsOut(digits=digits, min=None, max=None, avg=None)

    min_digit = min(digits)
    max_digit = max(digits)
    avg = sum(digits) / len(digits)

    return DigitsOut(digits=digits, min=min_digit, max=max_digit, avg=avg)
