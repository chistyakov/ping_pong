from os import getenv
from random import randint

import aiohttp
from fastapi import FastAPI, BackgroundTasks

from common.const import DIGIT_MIN, DIGIT_MAX
from common.schema import DigitsIn as Digits

app = FastAPI()


async def pong(digits: Digits) -> None:
    async with aiohttp.ClientSession(raise_for_status=True) as session:
        await session.post(f"{getenv('SERVICE_B_BASE_URL')}/pong", json=digits.dict())


@app.post("/ping")
def post_ping(digits_input: Digits, background_tasks: BackgroundTasks) -> Digits:
    new_value = randint(DIGIT_MIN, DIGIT_MAX)

    digits_list = digits_input.digits or []
    digits_list.append(new_value)
    digits_output = Digits(digits=digits_list)

    background_tasks.add_task(pong, digits=digits_output)

    return digits_output
