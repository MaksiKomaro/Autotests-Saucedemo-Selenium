from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    """Начальная страница после авторизации
    """
    TITLE_TEXT = 'Products'

    BURGER_BTN = (By.ID, 'react-burger-menu-btn')
    CART_BTN = (By.ID, 'shopping_cart_container')
    TITLE_FIELD = (By.CLASS_NAME, 'title')

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def verify_main_page(self):
        return all(
            (
                self.locate_element(self.BURGER_BTN),
                self.locate_element(self.CART_BTN),
                self.locate_element(self.TITLE_FIELD),
            )
        )
