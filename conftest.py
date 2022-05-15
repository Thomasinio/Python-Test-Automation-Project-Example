import pytest
import allure
from pathlib import Path
from loguru import logger

from core.api_client import ApiClient


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # Set a report attribute for each phase of a call, which can be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="session")
def authorized_api_client():
    yield ApiClient().authorize()


@pytest.fixture(autouse=True)
def write_logs(request):
    # put logs in tests/logs
    log_path = Path("logs")

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
    logger.configure(handlers=[{"sink": log_path, "level": "TRACE", "mode": "w", "backtrace": False}])
    logger.enable("my_package")

    yield

    if request.node.rep_call.failed:
        allure.attach.file(log_path, "Logs", allure.attachment_type.TEXT)
