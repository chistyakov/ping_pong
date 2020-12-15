from os import getenv
from typing import List

import aiohttp

from common.const import DEFAULT_SERVICE_B_BASE_URL
from common.tracing.x_correlation_id import get_x_correlation_id
from common.url import build_url


async def pong(digits_list: List[int], aiohttp_client: aiohttp.ClientSession) -> None:
    response = await aiohttp_client.post(
        url=build_url(
            getenv("SERVICE_B_BASE_URL", DEFAULT_SERVICE_B_BASE_URL), "/pong"
        ),
        json={"digits": digits_list},
        headers={"x-correlation-id": get_x_correlation_id()},
    )
    response.raise_for_status()
