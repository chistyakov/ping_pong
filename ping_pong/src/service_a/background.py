from os import getenv
from typing import List

import aiohttp


async def pong(digits_list: List[int], aiohttp_client: aiohttp.ClientSession) -> None:
    response = await aiohttp_client.post(
        f"{getenv('SERVICE_B_BASE_URL')}/pong", json={"digits": digits_list}
    )
    response.raise_for_status()
