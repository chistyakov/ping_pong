import aiohttp
from fastapi import Depends
from starlette.background import BackgroundTasks

from common.aiohttp_client import aiohttp_client
from common.schema import DigitsList
from service_b.background import ping
from service_b.core import get_avg_min_max
from service_b.schema import DigitsAvgMinMax


def post_pong(
    digits_input: DigitsList,
    background_tasks: BackgroundTasks,
    aiohttp_client: aiohttp.ClientSession = Depends(aiohttp_client),
) -> DigitsAvgMinMax:
    digits_list = digits_input.digits or []

    avg, min_digit, max_digit = get_avg_min_max(digits_list)

    background_tasks.add_task(
        ping, digits_list=digits_list, aiohttp_client=aiohttp_client
    )

    return DigitsAvgMinMax(digits=digits_list, min=min_digit, max=max_digit, avg=avg)
