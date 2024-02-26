import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BrowserDriver:
    _driver = None

    @classmethod
    def get_driver(cls, browser_name):
        if cls._driver is None:
            if browser_name == "chrome":
                options = Options()
                options.page_load_strategy = 'eager'
                cls._driver = webdriver.Chrome(options=options)
            elif browser_name == "firefox":
                options = webdriver.FirefoxOptions()
                options.page_load_strategy = 'eager'
                cls._driver = webdriver.Firefox(options=options)
            else:
                raise ValueError(
                    "Unsupported browser name. Use 'chrome' or 'firefox'."
                    )
        return cls._driver

    @classmethod
    def close_driver(cls):
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None
