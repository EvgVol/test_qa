from pages.main_page import MainPage
from pages.elements_page import ElementsPage
from pages.check_box_page import CheckBoxPage
import requests

LINK = 'https://demoqa.com/'


class TestCheckBox:
    def test_guest_should_see_elements_link(self, browser):
        main_page = MainPage(browser, LINK)
        main_page.open()
        main_page.should_be_correct_url(LINK)

    def test_guest_can_go_to_elements_link(self, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.click_to_button_elements()
        elements_page = ElementsPage(browser, browser.current_url)
        elements_page.should_have_elements_in_url()
        elements_page.should_have_check_box_button()

    def test_guest_can_click_check_box(self, browser):
        check_box = CheckBoxPage(browser, browser.current_url)
        check_box.click_to_button_check_box()
        check_box.should_have_check_box_in_url()
        check_box.should_have_correct_content_check_box()

    def test_guest_can_open_home_directory(self, browser):
        home_directory = CheckBoxPage(browser, browser.current_url)
        home_directory.click_to_open_home_folder()
        home_directory.should_be_expanded_home_directory()

    def test_guest_should_see_open_downloads_directory(self, browser):
        download_directory = CheckBoxPage(browser, browser.current_url)
        download_directory.should_be_open_downloads_directory()

    def test_guest_can_select_word_file(self, browser):
        check_box = CheckBoxPage(browser, browser.current_url)
        check_box.select_word_file()
        check_box.get_success_message()
