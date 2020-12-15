import logging
from contextvars import ContextVar, Token
from uuid import uuid4

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

_x_correlation_id: ContextVar[str] = ContextVar("x_correlation_id")


def get_x_correlation_id() -> str:
    return _x_correlation_id.get("NO-X-CORRELATION-ID")


def set_x_correlation_id(value: str) -> Token:
    return _x_correlation_id.set(value)


def reset_x_correlation_id(token: Token):
    _x_correlation_id.reset(token)


class XCorrelationIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        x_correlation_id = request.headers.get("x-correlation-id", str(uuid4()))
        token = set_x_correlation_id(x_correlation_id)
        response = await call_next(request)
        response.headers["x-correlation-id"] = x_correlation_id
        reset_x_correlation_id(token)
        return response


class XCorrelationIdFilter(logging.Filter):
    def filter(self, record) -> bool:
        record.x_correlation_id = get_x_correlation_id()
        return True
