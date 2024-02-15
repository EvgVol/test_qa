from selenium.webdriver.common.by import By


class MainPageLocators():
    """Селекторы на главной странице."""

    LINK_ELEMENTS = (By.XPATH, "//h5[contains(text(), 'Elements')]")


class ElementPageLocators():
    """Селекторы на странице `Elements`."""

    BUTTON_CHECK_BOX = (By.XPATH, "//span[contains(text(), 'Check Box')]")
    

class CheckBoxPageElements():
    """Селекторы на странице `Check Box`."""
    TITLE = (By.TAG_NAME, 'h1')
    BUTTON_PLUS = (By.CSS_SELECTOR, "path[d='M19 3H5c-1.11 0-2 .9-2 2v14c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-2 10h-4v4h-2v-4H7v-2h4V7h2v4h4v2z']")
    CHECK_BOX_WORD_FILE = (By.CSS_SELECTOR, "label[for=tree-node-wordFile] > span > svg > path[d='M19 5v14H5V5h14m0-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2z']")
    RESULT = (By.CLASS_NAME, "text-success")
