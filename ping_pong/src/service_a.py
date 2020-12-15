from os import getenv
from random import randint

import aiohttp
from fastapi import FastAPI, BackgroundTasks
from fastapi.param_functions import Depends
from starlette.requests import Request

from common.const import DIGIT_MIN, DIGIT_MAX
from common.schema import DigitsIn as Digits


async def on_start_up():
    app.state.aiohttp_client = aiohttp.ClientSession()


async def on_shutdown():
    await app.state.aiohttp_client.close()


async def aiohttp_client(request: Request) -> aiohttp.ClientSession:
    return request.app.state.aiohttp_client


app = FastAPI(on_startup=[on_start_up], on_shutdown=[on_shutdown])


async def pong(digits: Digits, aiohttp_client: aiohttp.ClientSession) -> None:
    response = await aiohttp_client.post(
        f"{getenv('SERVICE_B_BASE_URL')}/pong", json=digits.dict()
    )
    response.raise_for_status()


@app.post("/ping")
def post_ping(
    digits_input: Digits,
    background_tasks: BackgroundTasks,
    aiohttp_client: aiohttp.ClientSession = Depends(aiohttp_client),
) -> Digits:
    new_value = randint(DIGIT_MIN, DIGIT_MAX)

    digits_list = digits_input.digits or []
    digits_list.append(new_value)
    digits_output = Digits(digits=digits_list)

    background_tasks.add_task(pong, digits=digits_output, aiohttp_client=aiohttp_client)

    return digits_output
