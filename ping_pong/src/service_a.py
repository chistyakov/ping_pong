from random import randint
from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel, validator

app = FastAPI()


DIGIT_MIN = 0
DIGIT_MAX = 100


class Digits(BaseModel):
    digits: Optional[List[int]]

    @validator("digits", each_item=True)
    def check_range(cls, v):
        assert (
            DIGIT_MIN <= v <= DIGIT_MAX
        ), f"{v} not in range ({DIGIT_MIN}, {DIGIT_MAX})"
        return v


@app.post("/ping")
def post_ping(digits_input: Digits):
    new_value = randint(DIGIT_MIN, DIGIT_MAX)

    digits = digits_input.digits or []
    digits.append(new_value)

    return {"digits": digits}
