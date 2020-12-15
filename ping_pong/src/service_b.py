from os import getenv
from typing import Optional, List

import aiohttp
from fastapi import FastAPI
from fastapi.param_functions import Depends
from pydantic import BaseModel
from starlette.background import BackgroundTasks
from starlette.requests import Request

from common.schema import DigitsIn


async def on_start_up():
    app.state.aiohttp_client = aiohttp.ClientSession()


async def on_shutdown():
    await app.state.aiohttp_client.close()


async def aiohttp_client(request: Request) -> aiohttp.ClientSession:
    return request.app.state.aiohttp_client


app = FastAPI(on_startup=[on_start_up], on_shutdown=[on_shutdown])


async def ping(digits: DigitsIn, aiohttp_client: aiohttp.ClientSession) -> None:
    response = await aiohttp_client.post(
        f"{getenv('SERVICE_A_BASE_URL')}/ping", json=digits.dict()
    )
    response.raise_for_status()


class DigitsOut(BaseModel):
    digits: Optional[List[int]]
    min: Optional[int]
    max: Optional[int]
    avg: Optional[float]


@app.post("/pong")
def post_ping(
    digits_input: DigitsIn,
    background_tasks: BackgroundTasks,
    aiohttp_client: aiohttp.ClientSession = Depends(aiohttp_client),
) -> DigitsOut:
    digits = digits_input.digits or []
    if not digits:
        return DigitsOut(digits=digits, min=None, max=None, avg=None)

    min_digit = min(digits)
    max_digit = max(digits)
    avg = sum(digits) / len(digits)

    background_tasks.add_task(ping, digits=digits_input, aiohttp_client=aiohttp_client)

    return DigitsOut(digits=digits, min=min_digit, max=max_digit, avg=avg)
