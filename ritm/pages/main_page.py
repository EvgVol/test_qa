from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    def should_be_link_to_page_elements(self):
        elements_link = self.is_element_present(
            *MainPageLocators.LINK_ELEMENTS
        )
        self.browser.execute_script("window.scrollBy(0, 100);")
        assert elements_link, (
            "Elements link is not presented"
        )

    def go_to_link_page(self):
        elements_link = self.browser.find_element(
            *MainPageLocators.LINK_ELEMENTS
        )
        self.browser.execute_script("window.scrollBy(0, 100);")
        elements_link.click()
