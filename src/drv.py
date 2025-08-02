from selenium.webdriver import Chrome, ChromeOptions

class ChromeDriver(Chrome):
    """Хром драйвер
    """
    def __init__(self, options = None, service = None, keep_alive = True):
        if options is None:
            options = ChromeOptions()
            options.add_experimental_option("excludeSwitches", ["enable-logging"])

        super().__init__(options, service, keep_alive)
        self.implicitly_wait(0.5)
        