import os
from time import sleep, strftime
import pytest
from pytest import TestReport, Item, CallInfo, FixtureRequest
from pluggy import Result
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

@pytest.fixture(scope="function", autouse=True)
def test_failed_check(request: FixtureRequest, browser: ChromeDriver):
    yield
    if request.node.rep_call.failed:
        sleep(1)
        time = strftime('%d.%m.%Y_%H_%M_%S')
        filename = f'{time}_{request.node.func_name}'
        save_screenshot(browser, filename)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: Item, call: CallInfo):
    """Добавляем результат теста в атрибут Item
    """
    y: Result = yield
    rep: TestReport = y.get_result()
    #if rep.failed and rep.when == 'call':
    setattr(item, 'rep_' + rep.when, rep)
    setattr(item, 'func_name', item.nodeid.split('::')[1])

def save_screenshot(browser: ChromeDriver, filename):
    folder = 'screenshots'
    os.makedirs(folder, exist_ok=True)
    filename = os.path.join(folder, f'{filename}.png')
    browser.save_screenshot(filename)
