from selenium.webdriver.common.by import By


class MainPageLocators():
    """Селекторы на главной странице."""

    LINK_ELEMENTS = (By.CSS_SELECTOR, ".top-card:nth-of-type(1)")


class ElementPageLocators():
    """Селекторы на странице `Elements`."""

    BUTTON_CHECK_BOX = (By.XPATH, "//span[contains(text(), 'Check Box')]")


class CheckBoxPageElements():
    """Селекторы на странице `Check Box`."""

    TITLE_CHECK_BOX = (By.TAG_NAME, 'h1')
    TREE_CHECK_BOX = (By.CLASS_NAME, 'check-box-tree-wrapper')
    COLLAPSED_TREE = (By.CLASS_NAME, 'rct-node-collapsed')
    EXPANDED_TREE = (By.CSS_SELECTOR, 'li.rct-node-expanded > ol')
    BUTTON_PLUS = (By.CSS_SELECTOR, "[aria-label='Expand all']")
    DOWNLOAD_DIRECTORY = (By.CSS_SELECTOR,
                          "li.rct-node-expanded:nth-of-type(3) ol")
    UNCHECK_BOX_WORD_FILE = (
        By.CSS_SELECTOR, "[for='tree-node-wordFile'] > span:nth-of-type(1)"
    )
    CHECK_BOX_WORD_FILE = (By.CLASS_NAME, "rct-icon-check")
    RESULT_SELECTED = (By.CLASS_NAME, "text-success")
