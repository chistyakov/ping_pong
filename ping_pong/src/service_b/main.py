from fastapi import FastAPI

from common.aiohttp_client import setup_http_client
from common.history import setup_response_history
from common.tracing.setup import setup_tracing
from service_b.route import setup_routes


def create_app() -> FastAPI:
    app = FastAPI(title="Service B")
    app = setup_tracing(app)
    app = setup_http_client(app)
    app = setup_routes(app)
    app = setup_response_history(app)
    return app
