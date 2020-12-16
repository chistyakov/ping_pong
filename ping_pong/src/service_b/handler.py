import aiohttp
from fastapi import Depends
from starlette.background import BackgroundTasks

from common.aiohttp_client import aiohttp_client_dep
from common.history import response_history_dep, ResponseHistory
from common.schema import DigitsInput, ResponseHistoryOutput
from service_b.background import ping
from service_b.core import get_avg_min_max
from service_b.schema import DigitsOutput


def post_pong(
    digits_input: DigitsInput,
    background_tasks: BackgroundTasks,
    aiohttp_client: aiohttp.ClientSession = Depends(aiohttp_client_dep),
    history: ResponseHistory = Depends(response_history_dep),
) -> DigitsOutput:
    digits_list = digits_input.digits or []

    avg, min_digit, max_digit = get_avg_min_max(digits_list)

    background_tasks.add_task(
        ping, digits_list=digits_list, aiohttp_client=aiohttp_client, history=history
    )

    return DigitsOutput(digits=digits_list, min=min_digit, max=max_digit, avg=avg)


def get_responses_history(
    x_correlation_id_arg: str, history: ResponseHistory = Depends(response_history_dep)
) -> ResponseHistoryOutput:
    return ResponseHistoryOutput(items=history.get_as_list(x_correlation_id_arg))
