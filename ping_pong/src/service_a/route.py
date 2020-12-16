from fastapi import FastAPI

from common.const import MAX_RESPONSE_HISTORY_SIZE
from service_a.handler import post_ping, get_responses_history


def setup_routes(app: FastAPI) -> FastAPI:
    app.router.add_api_route(path="/ping", endpoint=post_ping, methods=["POST"])
    app.router.add_api_route(
        path="/service_b_responses/{x_correlation_id_arg}",
        endpoint=get_responses_history,
        methods=["GET"],
        summary=f"Get last {MAX_RESPONSE_HISTORY_SIZE} responses from Service B by X-Correlation-Id",
    )
    return app
