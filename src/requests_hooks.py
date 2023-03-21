from loguru import logger
from pprint import pformat
from requests import Response


def check_for_error(response: Response, *args, **kwargs):
    # Each response is checked that the response HTTP status code is not a 4xx or a 5xx
    response.raise_for_status()


def response_logging_hook(response: Response, *args, **kwargs):
    logger.debug(response.url)
    logger.debug(response.status_code)
    logger.debug("\n" + pformat(response.json()))
