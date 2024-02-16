from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    """Методы для работы на главной странице."""

    def click_to_button_elements(self):
        self.click_to_link(MainPageLocators.LINK_ELEMENTS)

    def should_be_correct_url(self, link: str):
        assert self.browser.current_url == link, (
            "The current page URL does not match the expected URL"
        )
