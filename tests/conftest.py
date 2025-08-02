import pytest
from src.drv import ChromeDriver
from pages.all_pages_init import Pages


@pytest.fixture(scope='session')
def browser():
    browser = ChromeDriver()
    browser.maximize_window()
    browser.get('https://www.saucedemo.com/')
    yield browser
    browser.close()
    browser.quit()

@pytest.fixture(scope='session')
def pages(browser):
    pages = Pages(browser)
    yield pages
