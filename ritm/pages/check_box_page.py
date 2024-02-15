from pages.base_page import BasePage
from pages.locators import ElementPageLocators, CheckBoxPageElements


class CheckBoxPage(BasePage):
    
    def click_to_check_box(self):
        self.browser.find_element(
            *ElementPageLocators.BUTTON_CHECK_BOX
        ).click()

    def have_check_box_in_to_url(self):
        assert "checkbox" in self.browser.current_url, (
            "The checkbox is missing in the url"
        )

    def should_be_see_title_check_box(self):
        assert "Check Box" == self.browser.find_element(
            *CheckBoxPageElements.TITLE
        ).text, "The title on the page is incorrect"

    def click_on_the_button_to_open_the_home_folder(self):
        self.browser.find_element(
            *CheckBoxPageElements.BUTTON_PLUS
        ).click()
