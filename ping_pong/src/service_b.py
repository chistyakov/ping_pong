from os import getenv
from typing import Optional, List

import aiohttp
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.background import BackgroundTasks

from common.schema import DigitsIn

app = FastAPI()


async def ping(digits: DigitsIn) -> None:
    async with aiohttp.ClientSession(raise_for_status=True) as session:
        await session.post(f"{getenv('SERVICE_A_BASE_URL')}/ping", json=digits.dict())


class DigitsOut(BaseModel):
    digits: Optional[List[int]]
    min: Optional[int]
    max: Optional[int]
    avg: Optional[float]


@app.post("/pong")
def post_ping(digits_input: DigitsIn, background_tasks: BackgroundTasks) -> DigitsOut:
    digits = digits_input.digits or []
    if not digits:
        return DigitsOut(digits=digits, min=None, max=None, avg=None)

    min_digit = min(digits)
    max_digit = max(digits)
    avg = sum(digits) / len(digits)

    background_tasks.add_task(ping, digits=digits_input)

    return DigitsOut(digits=digits, min=min_digit, max=max_digit, avg=avg)
