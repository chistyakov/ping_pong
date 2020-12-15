import aiohttp
from fastapi import Depends
from starlette.background import BackgroundTasks

from common.aiohttp_client import aiohttp_client
from common.schema import DigitsInput
from service_b.background import ping
from service_b.core import get_avg_min_max
from service_b.schema import DigitsOutput


def post_pong(
    digits_input: DigitsInput,
    background_tasks: BackgroundTasks,
    aiohttp_client: aiohttp.ClientSession = Depends(aiohttp_client),
) -> DigitsOutput:
    digits_list = digits_input.digits or []

    avg, min_digit, max_digit = get_avg_min_max(digits_list)

    background_tasks.add_task(
        ping, digits_list=digits_list, aiohttp_client=aiohttp_client
    )

    return DigitsOutput(digits=digits_list, min=min_digit, max=max_digit, avg=avg)
