from selenium.webdriver import Chrome
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.start_page import StartPage


class Pages:
    def __init__(self, driver: Chrome):
        self.driver = driver
        self.cart_page = CartPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.start_page = StartPage(self.driver)
