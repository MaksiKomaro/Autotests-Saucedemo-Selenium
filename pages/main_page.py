from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    """Начальная страница после авторизации
    """
    LOGO_TEXT = 'Swag Labs'
    TITLE_TEXT = 'Products'

    BURGER_BTN = (By.ID, 'react-burger-menu-btn')
    CART_BTN = (By.ID, 'shopping_cart_container')
    TITLE_FIELD = (By.CLASS_NAME, 'title')
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '.inventory_item .btn_primary')
    RM_TO_CART_BTN = (By.CSS_SELECTOR, '.inventory_item .btn_secondary')
    CART_COUNTER = (By.CLASS_NAME, 'shopping_cart_badge')
    LOGO_FIELD = (By.CLASS_NAME, 'app_logo')

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
