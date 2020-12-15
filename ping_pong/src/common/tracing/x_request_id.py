import logging
from contextvars import ContextVar, Token
from uuid import uuid4

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

_x_request_id: ContextVar[str] = ContextVar("x_request_id")


def get_x_request_id() -> str:
    return _x_request_id.get("NO-X-REQUEST-ID")


def set_x_request_id(value: str) -> Token:
    return _x_request_id.set(value)


def reset_x_request_id(token: Token):
    _x_request_id.reset(token)


class XRequestIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        x_request_id = str(uuid4())
        token = set_x_request_id(x_request_id)
        response = await call_next(request)
        response.headers["x-request-id"] = x_request_id
        reset_x_request_id(token)
        return response


class XRequestIdFilter(logging.Filter):
    def filter(self, record) -> bool:
        record.x_request_id = get_x_request_id()
        return True
