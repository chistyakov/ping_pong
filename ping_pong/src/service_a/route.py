from fastapi import FastAPI

from service_a.handler import post_ping


def setup_routes(app: FastAPI) -> FastAPI:
    app.router.add_api_route(path="/ping", endpoint=post_ping, methods=["POST"])
    return app
