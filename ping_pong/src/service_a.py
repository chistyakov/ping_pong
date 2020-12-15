from os import getenv
from random import randint

import aiohttp
from fastapi import FastAPI, BackgroundTasks
from fastapi.param_functions import Depends

from common.aiohttp_client import setup_http_client, aiohttp_client
from common.const import DIGIT_MIN, DIGIT_MAX
from common.schema import DigitsIn as Digits


app = FastAPI()
app = setup_http_client(app)


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
