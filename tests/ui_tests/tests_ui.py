import pytest



@pytest.mark.UI
class TestsUI:


    def test_open_page(self, main_page):
        # Step 1
        page = main_page
        assert page.isDisplayedButtonShopAndSave() is True, "Error: Button “Shop & Save” not displayed"
        page.openWindow()
        page.clickCloseButton()
        assert page.isCloseed() is True, "Modal window is closed"
        # Step 2
        mattress_page = page.clickButtonShopAndSave()
        assert page.is_url_contain('/mattress'), "Page /mattress is not opened"
        # Step 3
        mattress_name = mattress_page.getMattressName()
        mattress_price = mattress_page.getMattressPrice()
        print( mattress_name, mattress_price)
        card_page = mattress_page.clickButtonAddToCard()
        assert page.is_url_contain('/checkout/shipping'), "Page /checkout is not opened"
        assert card_page.getName() is mattress_name
        assert card_page.getPrice() is mattress_price
