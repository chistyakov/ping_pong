from fastapi import FastAPI

from common.aiohttp_client import setup_http_client
from service_b.route import setup_routes


def create_app() -> FastAPI:
    app = FastAPI()
    app = setup_http_client(app)
    app = setup_routes(app)
    return app
