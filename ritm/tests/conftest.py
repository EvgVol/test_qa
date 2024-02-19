import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session", params=["chrome", "firefox"])
def browser(request):

    if request.param == "chrome":
        options = Options()
        options.page_load_strategy = 'eager'
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        options.page_load_strategy = 'eager'
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser

    print("\nquit browser..")
    browser.quit()
