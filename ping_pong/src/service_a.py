from random import randint

from fastapi import FastAPI

from common.const import DIGIT_MIN, DIGIT_MAX
from common.schema import DigitsIn as Digits

app = FastAPI()


@app.post("/ping")
def post_ping(digits_input: Digits) -> Digits:
    new_value = randint(DIGIT_MIN, DIGIT_MAX)

    digits = digits_input.digits or []
    digits.append(new_value)

    return Digits(digits=digits)
