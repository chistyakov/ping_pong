from fastapi import FastAPI

from common.const import MAX_RESPONSE_HISTORY_SIZE
from service_b.handler import post_pong, get_responses_history


def setup_routes(app: FastAPI) -> FastAPI:
    app.router.add_api_route(path="/pong", endpoint=post_pong, methods=["POST"])
    app.router.add_api_route(
        path="/service_a_responses/{x_correlation_id_arg}",
        endpoint=get_responses_history,
        methods=["GET"],
        summary=f"Get last {MAX_RESPONSE_HISTORY_SIZE} responses from Service A by X-Correlation-Id",
    )
    return app
