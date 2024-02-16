from pages.base_page import BasePage
from pages.locators import ElementPageLocators, CheckBoxPageElements


class CheckBoxPage(BasePage):
    """Методы для работы на странице CheckBox."""

    def click_to_button_check_box(self):
        self.click_to_link(ElementPageLocators.BUTTON_CHECK_BOX)

    def click_to_open_home_folder(self):
        self.click_to_link(CheckBoxPageElements.BUTTON_PLUS)

    def get_success_message(self):
        message = self.browser.find_element(
            *CheckBoxPageElements.RESULT_SELECTED
        )
        assert message.text == "wordFile", (
            "The user should see 'You have selected : wordFile'"
        )

    def should_have_correct_content_check_box(self):
        self.should_be_see_title_check_box()
        self.should_be_see_tree_check_box()
        self.should_be_collapsed_home_directory()

    def should_have_check_box_in_url(self):
        assert "checkbox" in self.browser.current_url, (
            "The checkbox is missing in the url"
        )

    def should_be_see_title_check_box(self):
        assert "Check Box" == self.browser.find_element(
            *CheckBoxPageElements.TITLE_CHECK_BOX
        ).text, "The title on the page is incorrect"

    def should_be_see_tree_check_box(self):
        self.is_element_present(
            CheckBoxPageElements.TREE_CHECK_BOX,
            "The checkbox does not contain a nesting tree"
        )

    def should_be_collapsed_home_directory(self):
        self.is_element_present(
            CheckBoxPageElements.COLLAPSED_TREE,
            "The home directory should be collapsed"
        )

    def should_be_expanded_home_directory(self):
        self.is_element_present(
            CheckBoxPageElements.EXPANDED_TREE,
            "The home directory should be expanded"
        )

    def should_be_open_downloads_directory(self):
        self.is_element_present(
            CheckBoxPageElements.DOWNLOAD_DIRECTORY,
            "Downloads directory should be open"
        )

    def select_word_file(self):
        self.click_to_link(CheckBoxPageElements.UNCHECK_BOX_WORD_FILE)
        self.is_element_present(
            CheckBoxPageElements.CHECK_BOX_WORD_FILE,
            "The word file don't check!"
        )
