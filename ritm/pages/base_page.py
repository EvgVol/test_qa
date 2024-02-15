from dataclasses import dataclass
from typing import Any

from selenium.common.exceptions import (NoSuchElementException)


@dataclass
class BasePage():
    """Необходимые методы для работы с webdriver."""

    browser: Any
    url: str
    timeout: int = 5

    def __post_init__(self) -> None:
        self.browser.implicitly_wait(self.timeout)

    def open(self) -> None:
        self.browser.get(self.url)

    def is_element_present(self, how: Any, what: str) -> bool:
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
