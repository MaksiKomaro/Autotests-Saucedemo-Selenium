import os
from selenium.webdriver import Chrome, ChromeOptions


class ChromeDriver(Chrome):
    """Хром драйвер
    """
    def __init__(self, options = None, service = None, keep_alive = True):
        if options is None:
            options = ChromeOptions()
            
            # Режим инкогнито, т.к. появляется менеджер паролей
            options.add_argument("--incognito")
            
            # Отключение логирования в консоль
            options.add_experimental_option("excludeSwitches", ["enable-logging"])

            if os.getenv('GITHUB_ACTIONS') == 'true':
                options.add_argument("--headless=new")

        super().__init__(options, service, keep_alive)
        self.implicitly_wait(0.5)
        