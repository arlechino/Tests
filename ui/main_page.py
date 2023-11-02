from ui.base_page import BasePage
from ui.mattress_page import MattressPage
from ui.component.modal_window import ModalWindow
from selenium.webdriver.common.by import By

class MainPage(ModalWindow):

    __button_shop_and_save = (By.CSS_SELECTOR, 'a[data-testid="hero_shop_mattress"]')


    def __init__(self, driver):
        super().__init__(driver)

    def isDisplayedButtonShopAndSave(self) -> bool:
        return self._is_displayed(self.__button_shop_and_save)

    def clickButtonShopAndSave(self):
        self._click(self.__button_shop_and_save)
        return MattressPage(self._driver)
