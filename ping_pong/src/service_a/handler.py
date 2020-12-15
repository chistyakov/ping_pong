import aiohttp
from fastapi import Depends
from starlette.background import BackgroundTasks

from common.aiohttp_client import aiohttp_client
from common.schema import DigitsInput, DigitsOutput
from service_a.background import pong
from service_a.core import append_new_digit


def post_ping(
    digits_input: DigitsInput,
    background_tasks: BackgroundTasks,
    aiohttp_client: aiohttp.ClientSession = Depends(aiohttp_client),
) -> DigitsOutput:
    digits_list = append_new_digit(digits_input.digits)

    background_tasks.add_task(
        pong, digits_list=digits_list, aiohttp_client=aiohttp_client
    )

    return DigitsOutput(digits=digits_list)
