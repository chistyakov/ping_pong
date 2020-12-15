import json
import logging
from typing import Callable

from fastapi.exceptions import RequestValidationError
from fastapi.routing import APIRoute
from starlette.requests import Request
from starlette.responses import Response

logger = logging.getLogger(__name__)


# Subclass route instead of middleware:
# https://github.com/tiangolo/fastapi/issues/954
class TracingRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            payload = await request.json()
            logger.debug("Request\n%s %s\n%s", request.method, request.url, payload)
            try:
                response = await original_route_handler(request)
            except RequestValidationError:
                logger.exception("Error handling %s %s", request.method, request.url)
                raise
            else:
                logger.debug(
                    "Response\n%s %s %s\n%s",
                    response.status_code,
                    request.method,
                    request.url,
                    json.loads(response.body),
                )
            return response

        return custom_route_handler
