import pytest
from utils.driver_factory import get_driver
import os

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs["driver"]
        os.makedirs("reports/screenshots", exist_ok=True)
        driver.save_screenshot(f"reports/screenshots/{item.name}.png")