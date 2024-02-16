from dataclasses import dataclass
from typing import Any, Tuple


@dataclass
class BasePage():
    """Методы для работы с webdriver."""

    browser: Any
    url: str
    timeout: int = 5

    def __post_init__(self):
        self.browser.implicitly_wait(self.timeout)

    def open(self):
        self.browser.get(self.url)

    def click_to_link(self, locator: Tuple[str, str]):
        element = self.browser.find_element(*locator)
        assert element.is_displayed(), (
            "The element is not displayed on the page."
        )
        self.browser.execute_script(
            'return arguments[0].scrollIntoView(true)', element
        )
        element.click()

    def is_element_present(self, locator: Tuple[str, str], message:str):
        assert self.browser.find_element(*locator).is_displayed(), message
