import aiohttp
from fastapi import Depends
from starlette.background import BackgroundTasks

from common.aiohttp_client import aiohttp_client_dep
from common.history import response_history_dep, ResponseHistory
from common.schema import DigitsInput, DigitsOutput, ResponseHistoryOutput
from service_a.background import pong
from service_a.core import append_new_digit


def post_ping(
    digits_input: DigitsInput,
    background_tasks: BackgroundTasks,
    aiohttp_client: aiohttp.ClientSession = Depends(aiohttp_client_dep),
    history: ResponseHistory = Depends(response_history_dep),
) -> DigitsOutput:
    digits_list = append_new_digit(digits_input.digits)

    background_tasks.add_task(
        pong,
        digits_list=digits_list,
        aiohttp_client=aiohttp_client,
        history=history,
    )

    return DigitsOutput(digits=digits_list)


def get_responses_history(
    x_correlation_id_arg: str, history: ResponseHistory = Depends(response_history_dep)
) -> ResponseHistoryOutput:
    return ResponseHistoryOutput(items=history.get_as_list(x_correlation_id_arg))
