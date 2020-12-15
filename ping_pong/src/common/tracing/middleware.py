from fastapi import FastAPI
from fastapi.param_functions import Depends, Header

from common.tracing.x_correlation_id import XCorrelationIdMiddleware
from common.tracing.x_request_id import XRequestIdMiddleware


# for X-Correlation-Id in swagger doc
def x_correlation_id(x_correlation_id: str = Header(None)):
    pass


def setup_tracing_middlewares(app: FastAPI) -> FastAPI:
    app.router.dependencies.append(Depends(x_correlation_id))
    app.add_middleware(XCorrelationIdMiddleware)
    app.add_middleware(XRequestIdMiddleware)
    return app
