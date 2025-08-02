from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class StartPage(BasePage):
    """Начальная страница авторизации https://www.saucedemo.com/
    """
    URL = 'https://www.saucedemo.com/'
    TITLE = 'Swag Labs'
    HEADER_TEXT = 'Swag Labs'

    HEADER = (By.CLASS_NAME, 'login_logo')
    USER_FIELD = (By.ID, 'user-name')
    PASS_FIELD = (By.ID, 'password')
    LOGIN_BTN = (By.ID, 'login-button')
    
    def __init__(self, driver):
        super().__init__(driver)
