from fastapi import FastAPI
from fastapi.param_functions import Depends, Header

from common.tracing.log_request_response import TracingRoute
from common.tracing.x_correlation_id import XCorrelationIdMiddleware
from common.tracing.x_request_id import XRequestIdMiddleware


# for the X-Correlation-Id header in Swagger doc
def x_correlation_id(x_correlation_id: str = Header(None)):
    pass


def setup_tracing(app: FastAPI) -> FastAPI:
    app.router.dependencies.append(Depends(x_correlation_id))
    app.add_middleware(XCorrelationIdMiddleware)

    app.add_middleware(XRequestIdMiddleware)

    app.router.route_class = TracingRoute
    return app
