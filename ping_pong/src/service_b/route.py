from fastapi import FastAPI

from service_b.handler import post_pong


def setup_routes(app: FastAPI) -> FastAPI:
    app.router.add_api_route(path="/pong", endpoint=post_pong, methods=["POST"])
    return app
