from selenium.webdriver import Chrome, Firefox, Edge
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options

class DriverFactory:
    CHROME = 1
    FIREFOX = 2
    EDGE = 3

    @staticmethod
    def create_driver(driver_id: int, is_headless=False):
        if int(driver_id) == 1:
            chrome_options = Options()
            if is_headless:
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--no-sandbox")
            driver = Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        elif int(driver_id) == 2:
            driver = Firefox(service=Service(GeckoDriverManager().install()))
        elif int(driver_id) == 3:
            driver = Edge(service=Service(EdgeChromiumDriverManager().install()))
        else:
            driver = Chrome(service=Service(ChromeDriverManager().install()))
        return driver
