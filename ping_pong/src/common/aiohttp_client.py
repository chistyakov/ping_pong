import logging
from types import SimpleNamespace

import aiohttp
from aiohttp import ClientSession, TraceRequestStartParams, TraceRequestEndParams
from fastapi import FastAPI
from starlette.requests import Request

logger = logging.getLogger(__name__)


async def aiohttp_client_dep(request: Request) -> aiohttp.ClientSession:
    return request.app.state.aiohttp_client


async def on_request_start(
    session: ClientSession,
    trace_config_ctx: SimpleNamespace,
    params: TraceRequestStartParams,
) -> None:
    logger.debug("Starting request %s %s", params.method, params.url)


async def on_request_end(
    session: ClientSession,
    trace_config_ctx: SimpleNamespace,
    params: TraceRequestEndParams,
) -> None:
    logger.debug(
        "Ending request %s %s %s", params.response.status, params.method, params.url
    )


def setup_http_client(app: FastAPI) -> FastAPI:
    trace_config = aiohttp.TraceConfig()
    trace_config.on_request_start.append(on_request_start)
    trace_config.on_request_end.append(on_request_end)

    async def on_app_start_up() -> None:
        app.state.aiohttp_client = aiohttp.ClientSession(trace_configs=[trace_config])

    async def on_app_shutdown() -> None:
        await app.state.aiohttp_client.close()

    app.add_event_handler("startup", on_app_start_up)
    app.add_event_handler("shutdown", on_app_shutdown)

    return app
