from pages.base_page import BasePage
from pages.locators import ElementPageLocators


class ElementsPage(BasePage):
    """Методы для работы на странице Elements."""

    def should_have_check_box_button(self):
        self.is_element_present(
            ElementPageLocators.BUTTON_CHECK_BOX,
            "The button check box is not displayed"
        )

    def should_have_elements_in_url(self):
        assert "elements" in self.browser.current_url, (
            "The elements is missing in the url"
        )
