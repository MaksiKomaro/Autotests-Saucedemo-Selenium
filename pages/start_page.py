from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class StartPage(BasePage):
    """Страница авторизации https://www.saucedemo.com/
    """
    URL = 'https://www.saucedemo.com/'
    TITLE = 'Swag Labs'
    HEADER_TEXT = 'Swag Labs'
    NO_USERNAME_TEXT = 'Epic sadface: Username is required'
    NO_PSWRD_TEXT = 'Epic sadface: Password is required'
    WRONG_CREDS = 'Epic sadface: Username and password do not match any user in this service'

    HEADER = (By.CLASS_NAME, 'login_logo')
    USER_FIELD = (By.ID, 'user-name')
    PASS_FIELD = (By.ID, 'password')
    LOGIN_BTN = (By.ID, 'login-button')
    ERR_CNTNR = (By.CLASS_NAME, 'error-message-container')
    ERR_TEXTFIELD = (By.CSS_SELECTOR, '.error-message-container h3')
    ERR_BTN = (By.CLASS_NAME, 'error-button')
    
    def __init__(self, driver):
        super().__init__(driver)
