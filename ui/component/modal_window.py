from ui.base_page import BasePage
from selenium.webdriver.common.by import By

class ModalWindow(BasePage):

    __veiw_part = (By.CSS_SELECTOR, "div.dy-modal-contents")
    __button_close = (By.CSS_SELECTOR, "div.dy-lb-close")

    def __init__(self, driver):
        super().__init__(driver, time_to_wait=10)

    def openWindow(self):
        self._wait_until_element_located(self.__veiw_part)

    def clickCloseButton(self):
        self._click(self.__button_close)

    def isCloseed(self):
        return self._is_disappeared(self.__veiw_part)
