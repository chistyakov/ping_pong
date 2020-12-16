from collections import deque, defaultdict
from json.decoder import JSONDecodeError
from time import time
from typing import List

from aiohttp import ClientResponse
from fastapi import FastAPI
from starlette.requests import Request

from common.const import MAX_RESPONSE_HISTORY_SIZE


class ResponseHistory:
    def __init__(self):
        self._history = defaultdict(lambda: deque(maxlen=MAX_RESPONSE_HISTORY_SIZE))

    async def add(self, x_correlation_id: str, response: ClientResponse) -> None:
        try:
            response_json = await response.json()
        except JSONDecodeError:
            response_json = None
        self._history[x_correlation_id].appendleft(
            (time(), response.status, response_json)
        )

    def get_as_list(self, x_correlation_id: str) -> List[dict]:
        items = []
        for timestamp, status, json in self[x_correlation_id]:
            items.append({"timestamp": timestamp, "status": status, "json": json})
        return items

    def __getitem__(self, item):
        return self._history[item]


async def response_history_dep(request: Request) -> ResponseHistory:
    return request.app.state.response_history


def setup_response_history(app: FastAPI) -> FastAPI:
    app.state.response_history = ResponseHistory()
    return app
