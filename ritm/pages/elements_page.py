from pages.base_page import BasePage
from pages.locators import ElementPageLocators


class ElementsPage(BasePage):

    def have_elements_in_to_url(self):
        assert "elements" in self.browser.current_url, (
            "The elements is missing in the url"
        )

    def should_be_button_a_check_box(self):
        assert self.is_element_present(
            *ElementPageLocators.BUTTON_CHECK_BOX
        ), "The button check box is not displayed"
