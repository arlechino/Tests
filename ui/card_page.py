from ui.base_page import BasePage
from selenium.webdriver.common.by import By

class CardPage(BasePage):

    __title = (By.CSS_SELECTOR, 'a.product-link-title_RHg')
    __price = (By.CSS_SELECTOR, 'div[data-testid="awara_latex_hybrid_mattress__price"] > ins')

    def __init__(self, driver):
        super().__init__(driver)

    def getName(self) -> str:
        return self._get_text(self.__title)

    def getPrice(self) -> str:
        return self._get_text(self.__price)
