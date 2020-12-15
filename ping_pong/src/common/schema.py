from typing import Optional, List

from pydantic import BaseModel, validator, Field

from common.const import DIGIT_MIN, DIGIT_MAX


class DigitsInput(BaseModel):
    digits: Optional[List[int]] = Field(example=[42])

    @validator("digits", each_item=True)
    def check_reach_digit_range(cls, v):
        assert (
            DIGIT_MIN <= v <= DIGIT_MAX
        ), f"{v} not in range ({DIGIT_MIN}, {DIGIT_MAX})"
        return v

    @validator("digits")
    def check_last_digit(cls, v):
        if not v:
            return v

        last_digit = v[-1]
        assert is_digit_valid(last_digit), f"Last digit in {v} is invalid"

        return v


def is_digit_valid(digit: int) -> bool:
    if digit > 10:
        return True

    if digit % 3 != 0:
        return True

    return False


class DigitsOutput(BaseModel):
    digits: List[int]
