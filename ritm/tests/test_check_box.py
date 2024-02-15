from pages.main_page import MainPage
from pages.elements_page import ElementsPage
from pages.check_box_page import CheckBoxPage


LINK = 'https://demoqa.com/'


class TestCheckBox:
    def test_guest_should_see_elements_link(self, browser):
        main_page = MainPage(browser, LINK)
        main_page.open()
        main_page.should_be_link_to_page_elements()

    def test_guest_can_go_to_elements_link(self, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.go_to_link_page()
        elements_page = ElementsPage(browser, browser.current_url)
        elements_page.have_elements_in_to_url()

    def test_guest_should_see_to_check_box(self, browser):
        elements_page = ElementsPage(browser, browser.current_url)
        elements_page.should_be_button_a_check_box()

    def test_guest_can_click_to_check_box(self, browser):
        check_box = CheckBoxPage(browser, browser.current_url)
        check_box.click_to_check_box()
        check_box.have_check_box_in_to_url()

    def test_guest_shoul_see_correct_content_check_box(self, browser):
        content = CheckBoxPage(browser, browser.current_url)
        content.should_be_see_title_check_box()
