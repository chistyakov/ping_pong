from fastapi import FastAPI

from common.aiohttp_client import setup_http_client
from common.tracing.middleware import setup_tracing_middlewares
from service_a.route import setup_routes


def create_app() -> FastAPI:
    app = FastAPI()
    app = setup_http_client(app)
    app = setup_routes(app)
    app = setup_tracing_middlewares(app)
    return app
