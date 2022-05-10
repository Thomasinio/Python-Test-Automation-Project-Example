import pytest
from pathlib import Path
from loguru import logger
from core.api_client import ApiClient
from core.game_api_client import GameApiClient


@pytest.fixture(scope="session")
def authorized_game_api_client():
    authorized_api_client = ApiClient().authorize()
    authorized_game_api_client = GameApiClient(authorized_api_client)
    yield authorized_game_api_client


@pytest.fixture(autouse=True)
def write_logs(request):
    # put logs in tests/logs
    log_path = Path("tests") / "logs"

    # tidy logs in subdirectories based on test module and class names
    module = request.module
    class_ = request.cls
    name = request.node.name + ".log"

    if module:
        log_path /= module.__name__.replace("tests.", "")
    if class_:
        log_path /= class_.__name__

    log_path.mkdir(parents=True, exist_ok=True)

    # append last part of the name
    log_path /= name

    # enable the logger
    logger.remove()
    logger.configure(handlers=[{"sink": log_path, "level": "TRACE", "mode": "w"}])
    logger.enable("my_package")
