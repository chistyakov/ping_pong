from random import randint
from typing import Optional, List

from common.const import DIGIT_MIN, DIGIT_MAX


def append_new_digit(digits_list: Optional[List[int]]) -> List[int]:
    new_digit = randint(DIGIT_MIN, DIGIT_MAX)
    digits_list = digits_list or []
    digits_list.append(new_digit)
    return digits_list
