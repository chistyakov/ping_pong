from os import getenv
from typing import List

import aiohttp


async def ping(digits_list: List[int], aiohttp_client: aiohttp.ClientSession) -> None:
    response = await aiohttp_client.post(
        f"{getenv('SERVICE_A_BASE_URL')}/ping", json={"digits": digits_list}
    )
    response.raise_for_status()
