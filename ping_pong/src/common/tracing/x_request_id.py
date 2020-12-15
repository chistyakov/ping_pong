from contextvars import ContextVar, Token
from uuid import uuid4
import logging

from starlette.middleware.base import BaseHTTPMiddleware

_x_request_id: ContextVar[str] = ContextVar("x_request_id")


def get_x_request_id():
    return _x_request_id.get("NO-X-REQUEST-ID")


def set_x_request_id(value: str) -> Token:
    return _x_request_id.set(value)


def reset_x_request_id(token: Token):
    _x_request_id.reset(token)


class XRequestIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        x_request_id = str(uuid4())
        token = set_x_request_id(x_request_id)
        response = await call_next(request)
        response.headers["x-request-id"] = x_request_id
        reset_x_request_id(token)
        return response


class XRequestIdFilter(logging.Filter):
    def filter(self, record):
        record.x_request_id = get_x_request_id()
        return True
