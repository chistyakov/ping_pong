import aiohttp
from fastapi import FastAPI
from starlette.requests import Request


async def aiohttp_client(request: Request) -> aiohttp.ClientSession:
    return request.app.state.aiohttp_client


def setup_http_client(app: FastAPI) -> FastAPI:
    async def on_start_up():
        app.state.aiohttp_client = aiohttp.ClientSession()

    async def on_shutdown():
        await app.state.aiohttp_client.close()

    app.add_event_handler("startup", on_start_up)
    app.add_event_handler("shutdown", on_shutdown)

    return app
