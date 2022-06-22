from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_bucket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_ADD_BTN)
        button.click()

    def should_cost_equal(self):
        item_basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        item_product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert item_basket_cost == item_product_cost, "Prices in basket and in product page isn't equal"

    def should_name_equal(self):
        items_strong = self.browser.find_elements(*ProductPageLocators.BASKET_STRONG_NAMES)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        names_equal = False
        for item_strong in items_strong:
            if item_strong.text == product_name:
                names_equal = True
        assert names_equal, "Names of product isn't equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BASKET_STRONG_NAMES), \
            "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.BASKET_STRONG_NAMES), \
            "Success message isn't disappeared"
