import pytest
from pages.web_driver import BrowserDriver


@pytest.fixture(scope="session", params=["chrome", "firefox"])
def browser(request):
    driver = BrowserDriver.get_driver(request.param)
    yield driver
    BrowserDriver.close_driver()
