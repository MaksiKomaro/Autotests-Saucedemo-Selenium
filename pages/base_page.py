from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Базовая страница модели POM
    """
    def __init__(self, driver: Chrome, timeout: int=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def open(self, url: str):
        self.driver.get(url)
    
    @property
    def get_title(self):
        return self.driver.title
    
    def screenshot(self, name):
        self.driver.save_screenshot(name)
    
    def locate_element(self, el: tuple):
        return self.wait.until(EC.presence_of_element_located(el))
    
    def clear_field(self, el):
        self.locate_element(el).clear()

    def click_element(self, el):
        self.locate_element(el).click()
    
    def get_text(self, el):
        return self.locate_element(el).text
    
    def send_text(self, el, text):
        self.locate_element(el).send_keys(text)
