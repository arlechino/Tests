from ui.base_page import BasePage
from ui.card_page import CardPage
from selenium.webdriver.common.by import By


class MattressPage(BasePage):

    __button_add_to_card = (By.CSS_SELECTOR, 'button[data-testid="addtocart_btn"]')
    __mattress_name = (By.CSS_SELECTOR, ' label[data-testid="awara-latex-hybrid-mattress"]'
                                        ' div.mattress-product__details__IB h3')
    __mattress_price = (By.CSS_SELECTOR, 'div[data-testid="cart-actions"] '
                                         'div[data-testid="add_to_cart_property_selector_size"] '
                            'span[data-testid="add_to_cart_property_selector_size_selected_original_price"]')

    def __init__(self, driver):
        super().__init__(driver)

    def clickButtonAddToCard(self):
        self._click(self.__button_add_to_card)
        return CardPage(self._driver)

    def getMattressName(self) -> str:
        return self._get_text(self.__mattress_name)

    def getMattressPrice(self) -> str:
        return self._get_text(self.__mattress_price)
