from selenium.webdriver.common.by import By


class ProductPageLocators:
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alertinner p strong")
    BASKET_ADD_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    BASKET_STRONG_NAMES = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
