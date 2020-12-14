from typing import Optional, List

from pydantic import BaseModel, validator

from common.const import DIGIT_MIN, DIGIT_MAX


class DigitsIn(BaseModel):
    digits: Optional[List[int]]

    @validator("digits", each_item=True)
    def check_range(cls, v):
        assert (
            DIGIT_MIN <= v <= DIGIT_MAX
        ), f"{v} not in range ({DIGIT_MIN}, {DIGIT_MAX})"
        return v
