from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_product(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_HAS_PRODUCT), \
            "Product is here, but should not be"

    def should_not_be_basket_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), \
            "Empty message is not presented, but should be"
