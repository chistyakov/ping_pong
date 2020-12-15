from os import getenv
from typing import List

import aiohttp

from common.tracing.x_correlation_id import get_x_correlation_id


async def pong(digits_list: List[int], aiohttp_client: aiohttp.ClientSession) -> None:
    response = await aiohttp_client.post(
        f"{getenv('SERVICE_B_BASE_URL')}/pong",
        json={"digits": digits_list},
        headers={"x-correlation-id": get_x_correlation_id()},
    )
    response.raise_for_status()
